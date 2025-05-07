![poggit-icon](https://github.com/user-attachments/assets/50006405-7390-4737-94bc-2e6efaaaa780)
![Python](https://github.com/user-attachments/assets/3948c9ed-d788-4616-a3a0-6d75612a9c16)

# poggit python API
a python wrapper for poggit dev https://poggit.pmmp.io/ci/recent search by name and retrieve details such as the plugin's name, author, type, and link, without captchas!

## requirements
- python 3.x
- `requests` 
- `bs4` 

install dependencies:

```bash
pip3 install requests bs4
```

## usage

1. **search in dev plugins by name**:

   ```python
   poggit = PoggitAPI()
   plugins = poggit.get_dev_builds_by_name('easy')
   print(plugins)
   ```

   this will search for plugins with the keyword "easy" and print their details.

## features
- search for plugins by name.
- fetch plugin details: name, author, type, and link.
- automatically handles CSRF token for secure requests.

## example output

```json
[
    {
        "name": "Easy Plugin",
        "link": "https://poggit.pmmp.io/plugin/EasyPlugin",
        "author": "Author Name",
        "type": "Plugin"
    }
]
```
