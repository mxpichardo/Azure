# Log Analytics KQL function An ASIM function to get multiple watchlists in raw format

ARM template for deploying the Log Analytics KQL function An ASIM function to get multiple watchlists in raw format

This ASIM function reads multiple watchlists in raw format. The primary use case is giving an option for using multiple watchlist names for the same watchlist. It is more performant than using the general _GetWatchlist function.


The Advanced SIEM Information Model (ASIM) enables you to use and create source-agnostic content, simplifying your analysis of the data in your Microsoft Sentinel workspace.

For more information about Log Analytics functions refer to:

- [KQL user defined functions](https://docs.microsoft.com/azure/data-explorer/kusto/query/functions/user-defined-functions)
- [Managing user functions in Azure Monitor](https://docs.microsoft.com/azure/azure-monitor/logs/functions)

<br/>

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FASIM%2FLibrary%2FARM%2FASIM_GetWatchlistsRaw%2FASIM_GetWatchlistsRaw.json) [![Deploy to Azure Gov](https://aka.ms/deploytoazuregovbutton)](https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FAzure-Sentinel%2Fmaster%2FASIM%2FLibrary%2FARM%2FASIM_GetWatchlistsRaw%2FASIM_GetWatchlistsRaw.json)
