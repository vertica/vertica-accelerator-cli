# openapi_client.DcGraphGetReportBillingTotalSummaryV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_reports_billing_summary_total_get**](DcGraphGetReportBillingTotalSummaryV1Api.md#v1_vaas_reports_billing_summary_total_get) | **GET** /v1/vaas/reports/billing-summary-total | 


# **v1_vaas_reports_billing_summary_total_get**
> InlineResponse200 v1_vaas_reports_billing_summary_total_get(time_range=time_range)



Get a dc report billing total summary.

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
    api_instance = openapi_client.DcGraphGetReportBillingTotalSummaryV1Api(api_client)
    time_range = '3 months' # str | Time range for the report. (optional) (default to '3 months')

    try:
        api_response = api_instance.v1_vaas_reports_billing_summary_total_get(time_range=time_range)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DcGraphGetReportBillingTotalSummaryV1Api->v1_vaas_reports_billing_summary_total_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_range** | **str**| Time range for the report. | [optional] [default to &#39;3 months&#39;]

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

