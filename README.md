## Coin Scraper
<p>Crypto currency data scraping app</p>
<br />

<h3>Output</h3>

<table>
    <tr>
        <td>
            <p>request sent</p>
            <img src="images/image1.png" />
        </td>
        <td>
            <p>Job status</p>
            <img src="images/image2.png" />
        </td>
    </tr>
    <tr>
        <td>
            <p>Jobs in admin pannel</p>
            <img src="images/image3.png" />
        </td>
        <td>
            <p>Job details</p>
            <img src="images/image4.png" />
        </td>
    </tr>
    <tr >
        <td colspan="2">
            <p>Job output data</p>
            <img src="images/image5.png" />
        </td>
    </tr>
</table>


<h3>Installation</h3>

<p>1. install dependencies</p>

```
pip install -r requirements.txt
```

<p>2. start redis server</p>

```
$ redis-server
```

<p>3. run celery worker </p>

```
celery --app=coinscrapper worker --loglevel=info --pool=threads
```

<p>4. run app
<p>

    ```
    python manage.py runserver
    ```