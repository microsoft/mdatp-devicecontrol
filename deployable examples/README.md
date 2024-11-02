# Deployable Examples

Each sub-folder contains a single deployable example.


These examples can be deployed to Intune using `dc`

To deploy an example as-is using the logged in user's identity:

```
cd <examples dir>
dc apply -u
```

The examples can be modified and then changes are applied to Intune.  This creates a configuration-as-code workflow.

>[!NOTE]
> Use `dc apply -a` to run `dc` as an application in devops automation scenarios

After modifying the xlsx, run
```
dc init
```

This regenerates the `XML` while preserving the GUIDs of the groups and rules.

To apply the changes to Intune, run
```
dc apply -u
```

To delete the policies from Intune
1.  Unassign the policies.
2.  Run `dc delete -u`

This will delete all of objects created in Intun associated with the example.



## Creating a deployable examples

The examples are initialized from a source Excel spreadsheet located in each examples `src` folder.
When the example is initialized by running `dc init xlsx`, the following occurs:

- a `package.json` file is created as a package manifest
- groups in the spreadsheet are converted to `xml`
- rules and entries in the spreadsheet are converted to `xml`
- settings in the spreadsheet are stored in the `package.json`
- a `metadata.json` file is created to store additional deployment information.




## More information
- Installing and configuring dc
