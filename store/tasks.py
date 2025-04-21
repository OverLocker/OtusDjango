from celery import shared_task

@shared_task
def log_new_product(product_name):
    print(f'New product added: {product_name}')

