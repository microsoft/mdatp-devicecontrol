# Co-Pilot prompts

Here's some helpful prompts to use with co-pilot

## Create a Powershell Utility to Access Device Properties

```
Create a powershell program that uses System.Windows.Forms to show the currently connected PnP devices.
The form should have a tab for each USB and WPD.
On that tab should be a Devices table that contains a row for each devices of that class that are present only.
The columns should be the Class, FriendlyName, InstanceId, Caption property.
Below the devices table should be a Device Properties table.
When a user selects a row in the Devices table, all of the properties of the device are shown in Device Properties table.
The Device Properties table should have one row per property.
When a user selects a row in the Device Properties table, the value of the property is copied to the user's clipboard and the user receives a notification in a dialog box that includes the value that was copied.
The two tables should have a bolded label followed by instructions for the user to follow above the data.
There should be a OK button at the bottom of the form.
When generating the porewshell, use only approved powershell verbs, make sure that the [void]$form.ShowDialog() is the last line of the program, and in the add_CellClick methods, reference the $selectedRow from $args[0].CurrentRow.
Don't use padding.
```


### Result
```powershell
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Function to create the form
function New-Form {
    $form = New-Object System.Windows.Forms.Form
    $form.Text = "PnP Devices"
    $form.Size = New-Object System.Drawing.Size(800, 600)
    return $form
}

# Function to create the tab control
function New-TabControl {
    $tabControl = New-Object System.Windows.Forms.TabControl
    $tabControl.Dock = [System.Windows.Forms.DockStyle]::Top
    $tabControl.Height = 300
    return $tabControl
}

# Function to create a data grid view
function New-DataGridView {
    $dataGridView = New-Object System.Windows.Forms.DataGridView
    $dataGridView.Dock = [System.Windows.Forms.DockStyle]::Fill
    $dataGridView.AutoSizeColumnsMode = [System.Windows.Forms.DataGridViewAutoSizeColumnsMode]::Fill
    return $dataGridView
}

# Function to create a tab page
function New-TabPage {
    param ($deviceType)
    $tabPage = New-Object System.Windows.Forms.TabPage
    $tabPage.Text = $deviceType

    $label = New-Object System.Windows.Forms.Label
    $label.Text = "Devices - Select a device to view its properties"
    $label.Font = New-Object System.Drawing.Font("Arial", 10, [System.Drawing.FontStyle]::Bold)
    $label.Dock = [System.Windows.Forms.DockStyle]::Top
    $tabPage.Controls.Add($label)

    $dataGridView = New-DataGridView
    $tabPage.Controls.Add($dataGridView)
    return $tabPage
}

# Function to populate the data grid view with devices
function Update-DataGridView {
    param (
        [System.Windows.Forms.DataGridView]$dataGridView,
        [string]$deviceType
    )

    $dataGridView.Rows.Clear()
    $dataGridView.Columns.Clear()

    $devices = Get-PnpDevice -Class $deviceType | Where-Object { $_.Present -eq $true }
    if ($devices.Count -gt 0) {
        $columns = @("Class", "FriendlyName", "InstanceId", "Caption")
        foreach ($column in $columns) {
            $dataGridView.Columns.Add($column, $column)
        }

        foreach ($device in $devices) {
            $row = @()
            foreach ($column in $columns) {
                $row += $device.$column
            }
            $dataGridView.Rows.Add($row)
        }
    }
}

# Function to update the properties table
function Update-PropertiesTable {
    param (
        [System.Windows.Forms.DataGridView]$propertiesTable,
        [string]$instanceId
    )

    $propertiesTable.Rows.Clear()
    $propertiesTable.Columns.Clear()
    $propertiesTable.Columns.Add("Property", "Property")
    $propertiesTable.Columns.Add("Value", "Value")

    $device = Get-PnpDevice -InstanceId $instanceId
    foreach ($property in $device.PSObject.Properties) {
        $propertiesTable.Rows.Add($property.Name, $property.Value)
    }
}

# Main script
$form = New-Form
$tabControl = New-TabControl
$propertiesTable = New-DataGridView

$propertiesLabel = New-Object System.Windows.Forms.Label
$propertiesLabel.Text = "Device Properties - Select a property to copy its value"
$propertiesLabel.Font = New-Object System.Drawing.Font("Arial", 10, [System.Drawing.FontStyle]::Bold)
$propertiesLabel.Dock = [System.Windows.Forms.DockStyle]::Top

$okButton = New-Object System.Windows.Forms.Button
$okButton.Text = "OK"
$okButton.Dock = [System.Windows.Forms.DockStyle]::Bottom
$okButton.Add_Click({ $form.Close() })

$deviceTypes = @("USB", "WPD")
foreach ($deviceType in $deviceTypes) {
    $tabPage = New-TabPage -deviceType $deviceType
    $tabControl.TabPages.Add($tabPage)

    $dataGridView = $tabPage.Controls[1]
    $dataGridView.add_CellClick({
        $selectedRow = $args[0].CurrentRow
        if ($selectedRow -ne $null) {
            $instanceId = $selectedRow.Cells["InstanceId"].Value
            Update-PropertiesTable -propertiesTable $propertiesTable -instanceId $instanceId
        }
    })

    Update-DataGridView -dataGridView $dataGridView -deviceType $deviceType
}

$propertiesTable.add_CellClick({
    $selectedRow = $args[0].CurrentRow
    if ($selectedRow -ne $null) {
        $value = $selectedRow.Cells["Value"].Value
        [System.Windows.Forms.Clipboard]::SetText($value)
        [System.Windows.Forms.MessageBox]::Show("Property value copied to clipboard: $value", "Notification", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Information)
    }
})

$form.Controls.Add($propertiesLabel)
$form.Controls.Add($propertiesTable)
$form.Controls.Add($tabControl)
$form.Controls.Add($okButton)

$form.Add_Shown({$form.Activate()})
[void]$form.ShowDialog()


```

