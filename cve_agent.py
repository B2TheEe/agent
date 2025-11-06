from itertools import product
from trace import Trace
import requests
from agents import Agent, Runner, trace, function_tool
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import json
from dotenv import load_dotenv
load_dotenv()

@function_tool
def get_cpe(product: str) -> str:
     """
      CPE finder
     :param product: name of product
     :return: CPE
     """
     a = "https://services.nvd.nist.gov/rest/json/cpes/2.0?keywordSearch={0}&keywordExactMatch".format(product)
     x = requests.get(a)
     z = x.json()
     print(z)
     products = z["products"]
     if len(products) == 0:
         return "No CPE result"
     else:
         cpes = products[0]
         cpename = cpes["cpe"]["cpeName"]
         print(cpename)
         return cpename


@function_tool
def get_cve(product: str) -> str:
    """
    Get CVE's from a prpduct

    :param product: Name of the product
    :return: CVE's
    """
    r = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName={0}".format(product)
    x = requests.get(r)
    z = x.json()
    print(z)
    return z


async def main():
 cve_agent = Agent(name="CVE Agent",
                   instructions="""You will provide information about vulnerabilities from a specific product,  Your result is information about CVE's from the NVD. "
                                "Instructions:
1) First find the cpe of the product asked by the user using get_cpe. Print the result of the cpe."
2) Using the cpe you use find_cve to find vulnerabilities . Print this result as well """,
                   tools = [get_cpe,get_cve])
 with trace("Simple CVE agent"):
     result = await Runner.run(cve_agent, "Find all the vulnerabilities from Ubuntu Linux 24.04 LTS Edition")

     print(result)

if __name__ == "__main__":

    asyncio.run(main())
""" 
    This product uses the NVD API but is not endorsed or certified by the NVD."
    """