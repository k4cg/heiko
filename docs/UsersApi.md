# swagger_client.UsersApi

All URIs are relative to *https://maas.intern.k4cg.org/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UsersApi.md#users_get) | **GET** /users | List all users
[**users_post**](UsersApi.md#users_post) | **POST** /users | Add a new user
[**users_user_id_admin_set_put**](UsersApi.md#users_user_id_admin_set_put) | **PUT** /users/{userId}/admin/set | Promote a user to admin
[**users_user_id_admin_unset_put**](UsersApi.md#users_user_id_admin_unset_put) | **PUT** /users/{userId}/admin/unset | Remove admin capabilities from an user
[**users_user_id_credits_add_put**](UsersApi.md#users_user_id_credits_add_put) | **PUT** /users/{userId}/credits/add | Add users credits
[**users_user_id_credits_transfer_put**](UsersApi.md#users_user_id_credits_transfer_put) | **PUT** /users/{userId}/credits/transfer | Transfer credits
[**users_user_id_credits_withdraw_put**](UsersApi.md#users_user_id_credits_withdraw_put) | **PUT** /users/{userId}/credits/withdraw | Widthdraw users credits
[**users_user_id_delete**](UsersApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Delete user
[**users_user_id_get**](UsersApi.md#users_user_id_get) | **GET** /users/{userId} | Get user by user ID
[**users_user_id_password_put**](UsersApi.md#users_user_id_password_put) | **PUT** /users/{userId}/password | Change password for currently logged in user.
[**users_user_id_resetpassword_put**](UsersApi.md#users_user_id_resetpassword_put) | **PUT** /users/{userId}/resetpassword | Set password for user ID
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

# **users_user_id_admin_set_put**
> User users_user_id_admin_set_put(user_id)

Promote a user to admin

Promote a user to admin. This can only be done by other admin users.

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
user_id = 56 # int | The ID of the user to promote to admin

try:
    # Promote a user to admin
    api_response = api_instance.users_user_id_admin_set_put(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_admin_set_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user to promote to admin | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_admin_unset_put**
> User users_user_id_admin_unset_put(user_id)

Remove admin capabilities from an user

Remove admin capabilities from an user. This can only be done by other admin users.

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
user_id = 56 # int | The ID of the user to remove admin capabilities from

try:
    # Remove admin capabilities from an user
    api_response = api_instance.users_user_id_admin_unset_put(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_admin_unset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The ID of the user to remove admin capabilities from | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_credits_add_put**
> User users_user_id_credits_add_put(credits, user_id)

Add users credits

Add users credits. This can only be done by the logged in user or a admin.

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
credits = 56 # int | 
user_id = 56 # int | The ID of the user for which the credits should be changed

try:
    # Add users credits
    api_response = api_instance.users_user_id_credits_add_put(credits, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_credits_add_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credits** | **int**|  | 
 **user_id** | **int**| The ID of the user for which the credits should be changed | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_credits_transfer_put**
> TransferredCredits users_user_id_credits_transfer_put(credits, user_id)

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
credits = 56 # int | 
user_id = 56 # int | The ID of the user to transfer credits to

try:
    # Transfer credits
    api_response = api_instance.users_user_id_credits_transfer_put(credits, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_credits_transfer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credits** | **int**|  | 
 **user_id** | **int**| The ID of the user to transfer credits to | 

### Return type

[**TransferredCredits**](TransferredCredits.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_credits_withdraw_put**
> User users_user_id_credits_withdraw_put(credits, user_id)

Widthdraw users credits

Widthdraw users credits. A user can only withdraw as many credits as she currently has, if more than available are attempted to withdraw, an error is returned and no withdrawl performed. This can only be done by the logged in user or a admin.

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
credits = 56 # int | 
user_id = 56 # int | The ID of the user for which the credits should be changed

try:
    # Widthdraw users credits
    api_response = api_instance.users_user_id_credits_withdraw_put(credits, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_credits_withdraw_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credits** | **int**|  | 
 **user_id** | **int**| The ID of the user for which the credits should be changed | 

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
user_id = 56 # int | The ID of the user to be deleted

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
 **user_id** | **int**| The ID of the user to be deleted | 

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
user_id = 56 # int | The user ID that needs to be fetched

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
 **user_id** | **int**| The user ID that needs to be fetched | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_put**
> User users_user_id_password_put(password, passwordnew, passwordrepeat, user_id)

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
password = 'password_example' # str | 
passwordnew = 'passwordnew_example' # str | 
passwordrepeat = 'passwordrepeat_example' # str | 
user_id = 56 # int | The ID of the user for which the password should be changed

try:
    # Change password for currently logged in user.
    api_response = api_instance.users_user_id_password_put(password, passwordnew, passwordrepeat, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**|  | 
 **passwordnew** | **str**|  | 
 **passwordrepeat** | **str**|  | 
 **user_id** | **int**| The ID of the user for which the password should be changed | 

### Return type

[**User**](User.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_resetpassword_put**
> User users_user_id_resetpassword_put(passwordnew, passwordrepeat, user_id)

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
passwordnew = 'passwordnew_example' # str | 
passwordrepeat = 'passwordrepeat_example' # str | 
user_id = 56 # int | The ID of the user for which the password should be changed

try:
    # Set password for user ID
    api_response = api_instance.users_user_id_resetpassword_put(passwordnew, passwordrepeat, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_user_id_resetpassword_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passwordnew** | **str**|  | 
 **passwordrepeat** | **str**|  | 
 **user_id** | **int**| The ID of the user for which the password should be changed | 

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

