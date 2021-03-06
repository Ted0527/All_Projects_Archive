import json, jwt

from django.http import response
from django.test import TestCase, Client

from .models     import *
from my_settings import SECRET_KEY, ALGORITHM

class ProductsAppTest(TestCase):
    def setUp(self):
        Menu.objects.create(
            id   = 1,
            name = 'P'
        )

        Category.objects.create(
            id      = 1,
            name    = 'PA',
            menu_id = 1
        )

        Category.objects.create(
            id      = 2,
            name    = 'DO',
            menu_id = 1
        )

        SubCategory.objects.create(
            id          = 1,
            name        = 'PAK',
            category_id = 1
        )

        SubCategory.objects.create(
            id          = 2,
            name        = 'RAL',
            category_id = 1
        )

        SubCategory.objects.create(
            id          = 3,
            name        = 'MONS',
            category_id = 2
        )

        Product.objects.create(
            id                  = 1,
            name                = 'PAKA',
            price               = '9999.99',
            brand               = 'DW',
            description         = 'description',
            thumbnail_image_url = 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg',
            sub_category_id     = 1
        )

        Product.objects.create(
            id                  = 2,
            name                = 'RALO',
            price               = '9999.99',
            brand               = 'DW',
            description         = 'description',
            thumbnail_image_url = 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg',
            sub_category_id     = 2
        )

        Product.objects.create(
            id                  = 3,
            name                = 'DOPA',
            price               = '9999.99',
            brand               = 'DW',
            description         = 'description',
            thumbnail_image_url = 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg',
            sub_category_id     = 3
        )

    def tearDown(self):
        Product.objects.all().delete()
        Menu.objects.all().delete()
        Category.objects.all().delete()
        SubCategory.objects.all().delete()

    def test_success_product_list_view(self):
        client = Client()
        response = client.get('/products')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
            {
                "result" : [{
                    'id'                  : 1,
                    'name'                : 'PAKA',
                    'price'               : '9999.99',
                    'brand'               : 'DW',
                    'description'         : 'description',
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                },{
                    'id'                  : 2,
                    'name'                : 'RALO',
                    'price'               : '9999.99',
                    'brand'               : 'DW',
                    'description'         : 'description',
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                },{
                    'id'                  : 3,
                    'name'                : 'DOPA',
                    'price'               : '9999.99',
                    'brand'               : 'DW',
                    'description'         : 'description',
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                }]
            }
        )
    
    def test_success_product_list_view_by_sub_category_id(self):
        client   = Client()
        response = client.get('/products?sub_category_id=2')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
            {
                "result": [{
                    'id':2,
                    'name':'RALO',
                    'price':'9999.99',
                    'brand':'DW',
                    'description':'description',
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                }]
            }
        )

    def test_search_product_list_view(self):
        client   = Client()
        response = client.get('/products?search=PAKA')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
            {
                'result': [{
                    'id'                  : 1, 
                    'name'                : 'PAKA', 
                    'price'               : '9999.99', 
                    'brand'               : 'DW', 
                    'description'         : 'description', 
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                }]
            }
        )

    def test_success_product_list_view_by_category_id(self):
        client = Client()
        response = client.get('/products?category_id=1')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
            {
                'result': [{
                    'id'                  : 1, 
                    'name'                : 'PAKA', 
                    'price'               : '9999.99', 
                    'brand'               : 'DW', 
                    'description'         : 'description', 
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                },{
                    'id'                  : 2, 
                    'name'                : 'RALO', 
                    'price'               : '9999.99', 
                    'brand'               : 'DW', 
                    'description'         : 'description', 
                    'thumbnail_image_url' : 'https://raw.githubusercontent.com/Djangowon/TIL/main/image/15C58535-76A3-4A64-813A-3896D4A6DEE7.jpeg'
                }]
            }
        )
    
    
    def test_success_categories_view(self):
        client   = Client()
        response = client.get('/products/categories')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(),
            {
                'message': 'SUCCESS', 
                'result': [{
                    'id': 1,
                    'name': 'PA',
                    'sub_category': [
                        {
                        'id': 1, 
                        'name': 'PAK'
                        },{
                        'id': 2, 
                        'name': 'RAL'}]
                    },{
                    'id': 2, 
                    'name': 'DO', 
                    'sub_category': [
                        {
                        'id': 3,
                        'name': 'MONS'}]
                    }
                ]
            })

class ProductDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        Menu.objects.create(
            id   = 1,
            name = '???'
        )
        
        Category.objects.create(
            id      = 1,
            name    = '???',
            menu_id = 1
        )
        
        SubCategory.objects.create(
            id          = 1,
            name        = '??????',
            category_id = 1
        )
        
        Product.objects.create(
            id                  = 1,
            name                = '??????1',
            price               = 1111111.00,
            brand               = 'zara',
            description         = '??????1???????????????',
            thumbnail_image_url = 'http:??????1??????????????????',
            sub_category_id     = 1 
        )
        
        Product.objects.create(
            id                  = 2,
            name                = '??????2',
            price               = 222222.00,
            brand               = 'zara2',
            description         = '??????2???????????????',
            thumbnail_image_url = 'http:??????2??????????????????',
            sub_category_id     = 1
        )  
        
        Product.objects.create(
            id                  = 3,
            name                = '??????3',
            price               = 333333.00,
            brand               = 'zara3',
            description         = '??????3???????????????',
            thumbnail_image_url = 'http:??????3??????????????????',
            sub_category_id     = 1
        )  

        Product.objects.create(
            id                  = 4,
            name                = '??????4',
            price               = 444444.00,
            brand               = 'zara4',
            description         = '??????4???????????????',
            thumbnail_image_url = 'http:??????4??????????????????',
            sub_category_id     = 1
        )  
        
        Image.objects.create(
            image_url  = 'http:??????1?????????',
            product_id = 1
        )
        
        Image.objects.create(
            image_url  = 'http:??????5?????????',
            product_id = 1
        )
        
        Image.objects.create(
            image_url  = 'http:??????2?????????',
            product_id = 2
        )
        
        Image.objects.create(
            image_url  = 'http:??????3?????????',
            product_id = 3
        )
        
        Image.objects.create(
            image_url  = 'http:??????4?????????',
            product_id = 4
        )
        
    def tearDown(self):
        Menu.objects.all().delete()
        SubCategory.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Image.objects.all().delete()
        
    def test_product_detail_view_get_success(self):
        client   = Client()
        response = client.get('/products/1')
        self.assertEqual(response.json(),
            {
                'result' : {
                    'category_name'       : '???',
                    'sub_category_name'   : '??????',
                    'product_name'        : '??????1',
                    'price'               : 1111111,
                    'brand'               : 'zara',
                    'description'         : '??????1???????????????',
                    'thumbnail_image_url' : 'http:??????1??????????????????',
                    'image_url'           : ['http:??????1?????????', 'http:??????5?????????']
                }
            }
        )  

        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_get_doesnotexist(self):
        client   = Client()
        response = client.get('/products/5')
        self.assertEqual(response.json(),
            {
                'message': 'PRODUCT_DOESNOT_EXIST'
            }
        )
        self.assertEqual(response.status_code, 400)

class ReviewViewTest(TestCase):
    def setUp(self):
        self.hines_token = jwt.encode({'id':1}, SECRET_KEY, ALGORITHM)
        
        Menu.objects.create(
            id   = 1,
            name = '???'
        )
      
        Category.objects.create(
            id      = 1,
            name    = '???',
            menu_id = 1
        )

        SubCategory.objects.create(
            id          = 1,
            name        = '??????',
            category_id = 1
        )
       
        Product.objects.create(
            id                  = 1,
            name                = '??????1',
            price               = 1111111.00,
            brand               = 'zara',
            description         = '??????1???????????????',
            thumbnail_image_url = 'http:??????1??????????????????',
            sub_category_id     = 1 
        )
        
        Product.objects.create(
            id                  = 2,
            name                = '??????2',
            price               = 222222.00,
            brand               = 'zara2',
            description         = '??????2???????????????',
            thumbnail_image_url = 'http:??????2??????????????????',
            sub_category_id     = 1
        )  
        
        Product.objects.create(
            id                  = 3,
            name                = '??????3',
            price               = 333333.00,
            brand               = 'zara3',
            description         = '??????3???????????????',
            thumbnail_image_url = 'http:??????3??????????????????',
            sub_category_id     = 1
        )  
        
        Image.objects.create(
            id         = 1,
            image_url  = 'http:??????1?????????',
            product_id = 1
        )
        
        Image.objects.create(
            id         = 2,
            image_url  = 'http:??????5?????????',
            product_id = 1
        )
        
        Image.objects.create(
            id         = 3,
            image_url  = 'http:??????2?????????',
            product_id = 2
        )
        
        Image.objects.create(
            id         = 4,
            image_url  = 'http:??????3?????????',
            product_id = 3
        )
        
        User.objects.create(
            id       = 1,
            name     = '?????????',
            kakao_id = '1',
            email    = 'wonwoo@gmial.com'
        )
        
    def tearDown(self):
        Menu.objects.all().delete()
        Category.objects.all().delete()
        SubCategory.objects.all().delete()        
        Product.objects.all().delete()
        User.objects.all().delete()

    def test_review_view_test_post_success(self):
        client  = Client()
        headers = {'HTTP_Authorization' : self.hines_token}
        
        result = {
            'content'   : 'test111',
            'image_url' : 'test1'
        }
        
        response = client.post('/products/1/review', json.dumps(result), content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),
            {
                'message':'SUCCESS'
            }
        )

    def test_review_view_test_post_key_error(self):
        client  = Client()
        headers = {'HTTP_Authorization' : self.hines_token}

        result = {
            'con  ' : 'test111',
            'image' : 'test1'
        }
    
        response = client.post('/products/1/review', json.dumps(result), content_type='application/json', **headers)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message':'KEY_ERROR'
            }
        )

    def test_review_view_test_post_key_error(self):
        client  = Client()
        headers = {'HTTP_Authorization' : self.hines_token}

        result = {
            'con'       : 'test111',
            'image_url' : 'test1'
        }
    
        response = client.post('/products/1/review', json.dumps(result), content_type='application/json', **headers)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message':'KEY_ERROR'
            }
        )

    def test_review_view_test_post_invalid_product(self):
        client  = Client()
        headers = {'HTTP_Authorization' : self.hines_token}

        result = {
            'content'   : 'test111',
            'image_url' : 'test1'
        }
    
        response = client.post('/products/10/review', json.dumps(result), content_type='application/json', **headers)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message':'INAVID_PRODUCT_ID'
            }
        )