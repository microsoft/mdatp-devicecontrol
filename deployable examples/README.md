# Deployable Examples

The examples in this directory can be deployed to Intune using `dc`

To deploy an example using the logged in user's identity:

```
cd <examples dir>
dc apply -u
```
## Working with deployable examples

The examples are initialized from a source Excel spreadsheet located in each examples `src` folder.
When the example is initialized by running `dc init xlsx`, the following occurs:

- a `package.json` file is created as a package manifest
- groups in the spreadsheet are converted to `xml`
- rules and entries in the spreadsheet are converted to `xml`
- settings in the spreadsheet are stored in the `package.json`
- a `metadata.json` file is created to store additional deployment information.




## More information
- Installing and configuring dc
