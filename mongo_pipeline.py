# mongo_pipeline.py
from itemadapter import ItemAdapter
from models import Quote, Author

class MongoPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        if 'quote' in adapter:
            # Перевірка на унікальність цитати
            if not Quote.objects(quote=adapter['quote'], author=adapter['author']).first():
                Quote(
                    quote=adapter['quote'],
                    author=adapter['author'],
                    tags=adapter['tags']
                ).save()

        elif 'fullname' in adapter:
            # Перевірка на унікальність автора
            if not Author.objects(fullname=adapter['fullname']).first():
                Author(
                    fullname=adapter['fullname'],
                    born_date=adapter['born_date'],
                    born_location=adapter['born_location'],
                    description=adapter['description']
                ).save()

        return item
