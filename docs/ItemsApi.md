# swagger_client.ItemsApi

All URIs are relative to *https://maas.intern.k4cg.org/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_get**](ItemsApi.md#items_get) | **GET** /items | List all available items
[**items_item_id_consume_put**](ItemsApi.md#items_item_id_consume_put) | **PUT** /items/{itemId}/consume | Consumes a Item
[**items_item_id_delete**](ItemsApi.md#items_item_id_delete) | **DELETE** /items/{itemId} | Delete Item
[**items_item_id_get**](ItemsApi.md#items_item_id_get) | **GET** /items/{itemId} | Get a certain Item
[**items_item_id_put**](ItemsApi.md#items_item_id_put) | **PUT** /items/{itemId} | Update Item
[**items_item_id_stats_get**](ItemsApi.md#items_item_id_stats_get) | **GET** /items/{itemId}/stats | Get consumption stats
[**items_post**](ItemsApi.md#items_post) | **POST** /items | Add a new item
[**items_stats_get**](ItemsApi.md#items_stats_get) | **GET** /items/stats | Get consumption stats of all items

# **items_get**
> list[Item] items_get()

List all available items

Returns a map of item objects, with the item ID as key and the object as value

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))

try:
    # List all available items
    api_response = api_instance.items_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Item]**](Item.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_consume_put**
> ItemStats items_item_id_consume_put(item_id)

Consumes a Item

Consumes a Item and subtracts the cost of the Item from the credit of the user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | The ID of the Item that needs to be consumed

try:
    # Consumes a Item
    api_response = api_instance.items_item_id_consume_put(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_item_id_consume_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The ID of the Item that needs to be consumed | 

### Return type

[**ItemStats**](ItemStats.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_delete**
> Item items_item_id_delete(item_id)

Delete Item

Delete the Item. This can only be done by admins. (Should only mark a Item as deleted to not loose reference for stats)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | The ID of the Item that needs to be deleted

try:
    # Delete Item
    api_response = api_instance.items_item_id_delete(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_item_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The ID of the Item that needs to be deleted | 

### Return type

[**Item**](Item.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_get**
> Item items_item_id_get(item_id)

Get a certain Item

Get a certain Item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | The ID of the Item that needs to be fetched

try:
    # Get a certain Item
    api_response = api_instance.items_item_id_get(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_item_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The ID of the Item that needs to be fetched | 

### Return type

[**Item**](Item.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_put**
> Item items_item_id_put(name, cost, item_id)

Update Item

Update Item. This can only be done by admins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
cost = 56 # int | 
item_id = 56 # int | The ID of the Item that needs to be updated

try:
    # Update Item
    api_response = api_instance.items_item_id_put(name, cost, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_item_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **cost** | **int**|  | 
 **item_id** | **int**| The ID of the Item that needs to be updated | 

### Return type

[**Item**](Item.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_item_id_stats_get**
> ItemStats items_item_id_stats_get(item_id)

Get consumption stats

Get the matomat stats for a certain Item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
item_id = 56 # int | The ID of the Item for which to fetch the stats

try:
    # Get consumption stats
    api_response = api_instance.items_item_id_stats_get(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_item_id_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The ID of the Item for which to fetch the stats | 

### Return type

[**ItemStats**](ItemStats.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_post**
> Item items_post(name, cost)

Add a new item

Adds a new item to matomat. This can only be done by admins

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
cost = 56 # int | 

try:
    # Add a new item
    api_response = api_instance.items_post(name, cost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **cost** | **int**|  | 

### Return type

[**Item**](Item.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_stats_get**
> list[ItemStats] items_stats_get()

Get consumption stats of all items

Get the matomat stats for all items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsApi(swagger_client.ApiClient(configuration))

try:
    # Get consumption stats of all items
    api_response = api_instance.items_stats_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->items_stats_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ItemStats]**](ItemStats.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

