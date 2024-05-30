

enum MatchType {
    MatchAll
    MatchAny
}

class Group {
    [string] $id
    [string] $type
    [MatchType] $matchType
    [hashtable] $descriptors

    Group([System.Xml.XmlNode]$group_node) {

        $this.id = $group_node.Id
        $this.type = $group_node.Type
        $this.matchType = $group_node["MatchType"].InnerText
        $this.descriptors = @{}

        #Write-Host "Id=$($group_node.Id)"
        #Write-Host "MatchType=$($group_node["MatchType"].InnerText)"
        $descriptor_nodes = $group_node["DescriptorIdList"].ChildNodes  
        foreach($descriptor_node in $descriptor_nodes) {
            $descriptor_value = [System.Collections.ArrayList]@()
            if ($this.descriptors.ContainsKey($descriptor_node.LocalName)) {
                $descriptor_value = $this.descriptors[$descriptor_node.LocalName]
            }
            $descriptor_value.Add($descriptor_node.InnerText)
            $this.descriptors[$descriptor_node.LocalName] = $descriptor_value 
        }
        

    }
}

class Rule {

}

class Entry {

}

class Device {

}



function Get-DeviceControlGroups {

    $groups = Get-ItemPropertyValue "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Policy Manager" -Name PolicyGroups
    $groups > groups.xml
    $groups_xml = [xml](Get-Content .\groups.xml)

    $dc_groups = [System.Collections.ArrayList]@()



    $group_nodes = $groups_xml.SelectNodes("//Group")
    foreach ($group_node in $group_nodes) {
        
        $group = [Group]::new($group_node)

        $dc_groups.Add($group)

    }

    return $dc_groups

}

function Get-DeviceControlRules {

    $rules = Get-ItemPropertyValue "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Policy Manager" -Name PolicyRules
    $rules > rules.xml

    $rules_xml = [xml](Get-Content .\rules.xml)

}




#Get-PnpDevice -PresentOnly | ConvertTo-Json > devices.json
#$groups_xml | ConvertTo-Json > groups.json