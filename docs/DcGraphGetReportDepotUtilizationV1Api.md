# openapi_client.DcGraphGetReportDepotUtilizationV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_reports_dbname_depot_utilization_get**](DcGraphGetReportDepotUtilizationV1Api.md#v1_vaas_reports_dbname_depot_utilization_get) | **GET** /v1/vaas/reports/{dbname}/depot-utilization | 


# **v1_vaas_reports_dbname_depot_utilization_get**
> InlineResponse200 v1_vaas_reports_dbname_depot_utilization_get(dbname, module, time_range=time_range)



Get a dc report from certain database.

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
    api_instance = openapi_client.DcGraphGetReportDepotUtilizationV1Api(api_client)
    dbname = 'dbname_example' # str | 
module = 'vertica_cluster' # str | Name of the module. (default to 'vertica_cluster')
time_range = '1 month' # str | Time range for the report. (optional) (default to '1 month')

    try:
        api_response = api_instance.v1_vaas_reports_dbname_depot_utilization_get(dbname, module, time_range=time_range)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DcGraphGetReportDepotUtilizationV1Api->v1_vaas_reports_dbname_depot_utilization_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **module** | **str**| Name of the module. | [default to &#39;vertica_cluster&#39;]
 **time_range** | **str**| Time range for the report. | [optional] [default to &#39;1 month&#39;]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

