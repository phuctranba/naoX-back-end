from scrapy.exporters import CsvItemExporter


class Utf8CsvItemExporter(CsvItemExporter):

    def __init__(self, file, **kwargs):
        super(CsvItemExporter, self).__init__(
            file, ensure_ascii=False, **kwargs)
