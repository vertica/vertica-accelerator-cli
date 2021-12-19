# openapi_client.DcGraphBillingSummaryV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_reports_dbname_billing_summary_post**](DcGraphBillingSummaryV1Api.md#v1_vaas_reports_dbname_billing_summary_post) | **POST** /v1/vaas/reports/{dbname}/billing-summary | 


# **v1_vaas_reports_dbname_billing_summary_post**
> InlineResponse200 v1_vaas_reports_dbname_billing_summary_post(dbname)



Generate billing summary.

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
    api_instance = openapi_client.DcGraphBillingSummaryV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_response = api_instance.v1_vaas_reports_dbname_billing_summary_post(dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DcGraphBillingSummaryV1Api->v1_vaas_reports_dbname_billing_summary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 

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
**201** | Success created |  -  |
**412** | DC file not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

