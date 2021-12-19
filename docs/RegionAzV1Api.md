# openapi_client.RegionAzV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_config_region_az_region_get**](RegionAzV1Api.md#v1_vaas_config_region_az_region_get) | **GET** /v1/vaas/config/region_az/{region} | 


# **v1_vaas_config_region_az_region_get**
> v1_vaas_config_region_az_region_get(region)



Get a list of support AZs in the region.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.RegionAzV1Api(api_client)
    region = 'region_example' # str | 

    try:
        api_instance.v1_vaas_config_region_az_region_get(region)
    except ApiException as e:
        print("Exception when calling RegionAzV1Api->v1_vaas_config_region_az_region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

