from itertools import product
from trace import Trace
import requests
from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

from dotenv import load_dotenv
load_dotenv()

def get_cpe(product: str) -> str:
     """
      CPE finder
     :param product: name of product
     :return: CPE
     """
     a = "https://services.nvd.nist.gov/rest/json/cpes/2.0?keywordSearch={0}&keywordExactMatch".format(product)
     print(a)
     x = requests.get(a)
     print(x.status_code)
     print(x.request)


def get_cve(product: str) -> str:
    """
    Get CVE's from a prpduct

    :param product: Name of the product
    :return: CVE's
    """


async def main():
 cve_agent = Agent(name="CVE Agent", instructions="You will provide information about vulnerabilities from a specific product,  Your result is information about CVE's from the NVD. ")
 with trace("Simple CVE agent"):
     result = await Runner.run(cve_agent, "Find all the vulnerabilities from Apache")

     print(result)

if __name__ == "__main__":
    get_cpe("Ubuntu")

    """ 

    asyncio.run(main())

    
    This product uses the NVD API but is not endorsed or certified by the NVD."
    """