# swagger_client.UsersApi

All URIs are relative to *https://localhost:8443/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UsersApi.md#users_get) | **GET** /users | List all users
[**users_post**](UsersApi.md#users_post) | **POST** /users | Add a new user
[**users_user_id_credits_add_patch**](UsersApi.md#users_user_id_credits_add_patch) | **PATCH** /users/{userId}/credits/add | Add users credits
[**users_user_id_credits_transfer_patch**](UsersApi.md#users_user_id_credits_transfer_patch) | **PATCH** /users/{userId}/credits/transfer | Transfer credits
[**users_user_id_credits_withdraw_patch**](UsersApi.md#users_user_id_credits_withdraw_patch) | **PATCH** /users/{userId}/credits/withdraw | Widthdraw users credits
[**users_user_id_delete**](UsersApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Delete user
[**users_user_id_get**](UsersApi.md#users_user_id_get) | **GET** /users/{userId} | Get user by user ID
[**users_user_id_password_patch**](UsersApi.md#users_user_id_password_patch) | **PATCH** /users/{userId}/password | Change password for currently logged in user.
[**users_user_id_resetpassword_patch**](UsersApi.md#users_user_id_resetpassword_patch) | **PATCH** /users/{userId}/resetpassword | Set password for user ID
[**users_user_id_stats_get**](UsersApi.md#users_user_id_stats_get) | **GET** /users/{userId}/stats | Get matomat stats for user


# **users_get**
> list[User] users_get()

List all users

List all users

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # List all users
    api_response = api_instance.users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> User users_post(name, password, passwordrepeat, admin)

Add a new user

Add a new user. Only admin users are allowed to do this. If \"admin\" is greater than 0, the new user will be created as admin user.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
password = 'password_example' # str | 
passwordrepeat = 'passwordrepeat_example' # str | 
admin = 56 # int | 

try:
    # Add a new user
    api_response = api_instance.users_post(name, password, passwordrepeat, admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **password** | **str**|  | 
 **passwordrepeat** | **str**|  | 
 **admin** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_credits_add_patch**
> User users_user_id_credits_add_patch(user_id, credits)

Add users credits

Add users credits. This can only be done by the logged in user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The ID of the user for which the credits should be changed
credits = 56 # int | 

try:
    # Add users credits
    api_response = api_instance.users_user_id_credits_add_patch(user_id, credits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_credits_add_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user for which the credits should be changed | 
 **credits** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_credits_transfer_patch**
> TransferredCredits users_user_id_credits_transfer_patch(user_id, credits)

Transfer credits

Transfers credits from logged in user to given user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The ID of the user to transfer credits to
credits = 56 # int | 

try:
    # Transfer credits
    api_response = api_instance.users_user_id_credits_transfer_patch(user_id, credits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_credits_transfer_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user to transfer credits to | 
 **credits** | **int**|  | 

### Return type

[**TransferredCredits**](TransferredCredits.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_credits_withdraw_patch**
> User users_user_id_credits_withdraw_patch(user_id, credits)

Widthdraw users credits

Widthdraw users credits. A user can only withdraw as many credits as she currently has, if more than available are attempted to withdraw, an error is returned and no withdrawl performed. This can only be done by the logged in user

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The ID of the user for which the credits should be changed
credits = 56 # int | 

try:
    # Widthdraw users credits
    api_response = api_instance.users_user_id_credits_withdraw_patch(user_id, credits)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_credits_withdraw_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user for which the credits should be changed | 
 **credits** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> User users_user_id_delete(user_id)

Delete user

Delete user. This can only be done by the logged in user (for self) or an admin

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The user ID that to perform the operation on

try:
    # Delete user
    api_response = api_instance.users_user_id_delete(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user ID that to perform the operation on | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> User users_user_id_get(user_id)

Get user by user ID

Get user by user ID. Returns a user object

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The user ID that to perform the operation on

try:
    # Get user by user ID
    api_response = api_instance.users_user_id_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user ID that to perform the operation on | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_patch**
> User users_user_id_password_patch(user_id, password, passwordnew, passwordrepeat)

Change password for currently logged in user.

Change password for currently logged in user. Must provide old and new passwords (twice) in order to be allowed to change it.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The ID of the user for which the password should be changed
password = 'password_example' # str | 
passwordnew = 'passwordnew_example' # str | 
passwordrepeat = 'passwordrepeat_example' # str | 

try:
    # Change password for currently logged in user.
    api_response = api_instance.users_user_id_password_patch(user_id, password, passwordnew, passwordrepeat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_password_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user for which the password should be changed | 
 **password** | **str**|  | 
 **passwordnew** | **str**|  | 
 **passwordrepeat** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_resetpassword_patch**
> User users_user_id_resetpassword_patch(user_id, passwordnew, passwordrepeat)

Set password for user ID

Set password for user ID. This can only be done by a logged in admin for a different user than self.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The ID of the user for which the password should be changed
passwordnew = 'passwordnew_example' # str | 
passwordrepeat = 'passwordrepeat_example' # str | 

try:
    # Set password for user ID
    api_response = api_instance.users_user_id_resetpassword_patch(user_id, passwordnew, passwordrepeat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_resetpassword_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user for which the password should be changed | 
 **passwordnew** | **str**|  | 
 **passwordrepeat** | **str**|  | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_stats_get**
> UserStats users_user_id_stats_get(user_id)

Get matomat stats for user

Get the matomat stats for user. A user can only request the stats for herself

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 56 # int | The ID of the user for which to fetch the stats

try:
    # Get matomat stats for user
    api_response = api_instance.users_user_id_stats_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user for which to fetch the stats | 

### Return type

[**UserStats**](UserStats.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

