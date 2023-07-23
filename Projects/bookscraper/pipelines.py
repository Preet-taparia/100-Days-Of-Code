# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adaptor = ItemAdapter(item)

        field_names = adaptor.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adaptor.get(field_name)
                adaptor[field_name] = value.strip()


        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adaptor.get(lowercase_key)
            adaptor[lowercase_key] = value.lower()


        price_keys = ['price_excl_tax', 'price_incl_tax', 'tax', 'price']
        for price_key in price_keys:
            value = adaptor.get(price_key)
            value = value.replace('£', '')
            adaptor[price_key] = float(value)



        availability_string = adaptor.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adaptor['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adaptor['availability'] = int(availability_array[0])


        num_review_string = adaptor.get('num_reviews')
        adaptor['num_reviews'] = int(num_review_string)

        return item
