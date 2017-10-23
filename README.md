# scrapinhghub_download_api
Script that will download Scrapinghub spiders by job number.

To download finished Scrapinghub jobs simply edit the `download_spiders.py` file by adding a `apikey` and `project_number`.
Start the script with the first and last (inclusive) spider numbers as arguments. For example:

```shell
$ python3 download_spiders.py 100 110
```
