"""Fetch Google Scholar stats and write shields.io endpoint files.

Run by .github/workflows/google_scholar_crawler.yaml, which force-pushes the
results/ folder to the google-scholar-stats branch. The citation and h-index
badges on the site read their numbers from that branch, so they stay current
without anyone editing the page.
"""

import json
import os
from datetime import datetime

from scholarly import scholarly

author = scholarly.search_author_id(os.environ["GOOGLE_SCHOLAR_ID"])
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

author["updated"] = str(datetime.now())
author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)


def write_badge(filename, label, message):
    """Write a shields.io endpoint file (https://shields.io/endpoint)."""
    with open(f"results/{filename}", "w") as outfile:
        json.dump(
            {"schemaVersion": 1, "label": label, "message": str(message)},
            outfile,
            ensure_ascii=False,
        )


write_badge("gs_data_shieldsio.json", "citations", author["citedby"])
write_badge("gs_hindex_shieldsio.json", "h-index", author["hindex"])
write_badge("gs_i10index_shieldsio.json", "i10-index", author["i10index"])

print(
    f"{author['name']}: {author['citedby']} citations, "
    f"h-index {author['hindex']}, i10-index {author['i10index']}"
)
