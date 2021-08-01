# l<i>i</i>nkshr<i>i</i>nk
l<b>i</b>nkshr<b>i</b>nk: 
A url shortner

- naive implementation stores shortened urls in an in-memory dictionary
- actually works.

## Get code and run

```bash 
gh repo clone chrispydizzle/lnkshrnk
cd lnkshrnk
pip install -r requirements.txt
flask run
```

### Shrink something

```bash
curl http://localhost:5000/shrink -d '{ "url": "https://dogeplanet.com" }' -H 'Content-Type: application/json'
```
```json
{
  "url": "http://localhost:5000/go/5fd5085c"
}
```

### Unshrink something
Visiting the url will redirect you to the original url. But if you just want the original url 
```bash
curl http://localhost:5000/unshrink -d '{ "url": "http://localhost:5000/go/5fd5085c" }' -H 'Content-Type: application/json'
```

```json
{
  "url": "https://dogeplanet.com"
}
```


### Time spent

[![wakatime](https://wakatime.com/badge/github/chrispydizzle/lnkshrnk.svg)](https://wakatime.com/@ae6967d3-6d3b-4433-834a-e44dc28e320f/projects/hcqhowizas?start=2021-07-31&end=2021-07-31)

### More Project Information

- [Project](https://github.com/chrispydizzle/lnkshrnk/projects/1)
- [Wiki](https://github.com/chrispydizzle/lnkshrnk/wiki)
