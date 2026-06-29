import openpyxl

class ExcelUtils:

    @staticmethod
    def read_data(file, sheet, row, col):
        workbook = openpyxl.load_workbook(file)
        sh = workbook[sheet]
        return sh.cell(row, col).value