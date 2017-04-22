#coding:utf-8
import xlrd
import xlwt
# book=xlrd.open_workbook("demo.xls")#创建excel文件对象
# print book.sheets()#返回包含所有sheet对象的列表
# sheet=book.sheet_by_index(0)#通过索引值得到对应的sheet对象
# print sheet
# print sheet.nrows#表行数
# print sheet.ncols#表列数
# cell=sheet.cell(0,0)#得到某个单元格对象
# print cell.value#得到单元格的值
# print sheet.row(1)#返回一个列表获得某一行的所有单元格对象，
# print sheet.row_values(1)#返回一个列表包含某一行所有单元格的值
# print sheet.row_values(1,2)#可做切片操作
#sheet.col()用法同sheet.row()
# sheet.put_cell(0,sheet.ncols,xlrd.XL_CELL_TEXT,u"总分",None)#添加单元格
# wbook=xlwt.Workbook()#创建excel写对象
# wsheet=wbook.add_sheet("sheet1")#添加一个excel表
rbook=xlrd.open_workbook("demo.xls")
rsheet=rbook.sheet_by_index(0)
nc=rsheet.ncols
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,u"总分",None)
for row in xrange(1,69):
    t=sum(rsheet.row_values(row,2,5))
    rsheet.put_cell(row,nc,xlrd.XL_CELL_NUMBER,t,None)#在原文件中看不到所添加的单元格,
    # 只能在原文件中修改在新文件中生成
# print help(rsheet.row_values)
#写操作
wbook=xlwt.Workbook()
wsheet=wbook.add_sheet(rsheet.name)
style=xlwt.easyxf("align: vertical center, horizontal center")
for r in xrange(69):
    for c in xrange(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)
wbook.save("output.xls")


