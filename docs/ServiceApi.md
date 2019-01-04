# swagger_client.ServiceApi

All URIs are relative to *https://localhost:8443/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_stats_get**](ServiceApi.md#service_stats_get) | **GET** /service/stats | Total service stats


# **service_stats_get**
> ServiceStats service_stats_get()

Total service stats

Total service stats

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
api_instance = swagger_client.ServiceApi(swagger_client.ApiClient(configuration))

try:
    # Total service stats
    api_response = api_instance.service_stats_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->service_stats_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceStats**](ServiceStats.md)

### Authorization

[jwtTokenAuth](../README.md#jwtTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

