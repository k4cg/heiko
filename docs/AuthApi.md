# swagger_client.AuthApi

All URIs are relative to *https://maas.intern.k4cg.org/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](AuthApi.md#auth_login_post) | **POST** /auth/login | Logs a user in and returns an JWT token for authentication

# **auth_login_post**
> list[AuthSuccess] auth_login_post(username, password, validityseconds)

Logs a user in and returns an JWT token for authentication

Logs a user in and returns an JWT token for authentication. The passes along validitiyseconds determine how long the token should be available.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
username = 'username_example' # str | 
password = 'password_example' # str | 
validityseconds = 56 # int | 

try:
    # Logs a user in and returns an JWT token for authentication
    api_response = api_instance.auth_login_post(username, password, validityseconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **validityseconds** | **int**|  | 

### Return type

[**list[AuthSuccess]**](AuthSuccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

