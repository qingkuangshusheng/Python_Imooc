#coding:utf-8
import cv2#没有安装opencv
import os,cv2,time,struct,threading
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from SocketServer import  TCPServer,ThreadingTCPServer
from threading import Thread,RLock
from select import select

class JpegStreamer(Thread):
    def __init__(self,camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        print "self.cap is ",self.cap
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr,pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self,pr,pw):
        self.lock.acquire()
        self.pipes.pop(pr)
        self.lock.release()
        pr.close()
        pw.close()

    def capture(self):
        cap = self.cap
        print "cap.isOpened()",cap.isOpened()
        while cap.isOpened():
            print "frame is "
            print "ret is "
            ret, frame = cap.read()
            print "frame is ",frame
            print "ret is ",ret
            if ret:
                ret, data = cv2.imencode('.jpeg',frame,(cv2.IMWRITE_JPEG_QUALITY,40))
                yield data.tostring()

    def send(self,frame):
        n = struct.pack('l',len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _,pipes = select([],self.pipes.itervalues(),[],1)
            for pip in pipes:
                os.write(pip.n)
                os.write(pip,frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)

class JpegRetriever(object):
    def __init__(self,streamer):
        self.streamer = streamer
        self.local = threading.local()
        #self.pipe = streamer.register()

    def retrieve(self):
        while True:
            ns = os.read(self.pipe,8)
            n = struct.unpack('l',ns)[0]
            data = os.read(self.pipe,n)
            yield data

    def __enter__(self):
        if hasattr(self.local,'pip'):
            raise RuntimeError
        self.local.pipe = streamer.register()
        return self.retrieve()

    def cleanup(self):
        self.streamer.unregister(self.pipe)

    def __exit__(self,*args):
        self.streamer.unregister(self.local.pip)
        del self.local.pipe

class Handler(BaseHTTPRequestHandler):
    retriever = None
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    def do_GET(self):
        print "self.path is ",self.path
        if self.retriever is None:
            raise RuntimeError("no retriever")
        if self.path != '/':
            return
        self.send_response(200)
        self.send_header("Content-type",'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()
        with self.retriever as frames:
            for frame in frames:
                print "frame is coming..."
                self.send_frame(frame)

    def send_frame(self,frame):
        print "xxxxx"
        self.wfile.write('--abcde\r\n')
        self.wfile.write('Content-Type: image/jpeg/\r\n')
        self.wfile.write('Content-Length :%d\r\n\r\n' % len(frame))
        self.wfile.write(frame)

if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()
    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)
    print "starting server..."
    httpd = ThreadingTCPServer(('',9003),Handler)
    httpd.serve_forever()