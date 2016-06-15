# Scale R to Big Data Using Hadoop and Spark

Meetup Page: [http://www.meetup.com/data-science-dojo/events/231449206/](http://www.meetup.com/data-science-dojo/events/231449206/)

## Requirements
* Azure subscription or free trial account
	* [30 day free trial](https://azure.microsoft.com/en-us/pricing/free-trial/)
* Text Editor, I'll be using [Sublime Text 3]()
* Github.com account (to recieve code)
* PowerBI.com account (for Dashboard portion)
* .NET up to date + windows (for testing portion)

## Cloning the Repo for Code & Materials
```
git clone https://www.github.com/datasciencedojo/meetup.git
```
Folder: scaling\_r\_to\_big\_data

## Setting up an R Cluster

1. Sign in to the [Azure portal](https://portal.azure.com).

2. Select __NEW__, __Data + Analytics__, and then __HDInsight__.

    ![Image of creating a new cluster](/scaling_r_to_big_data/media/searchhdinsight.png)

3. Enter a name for the cluster in the __Cluster Name__ field. If you have multiple Azure subscriptions, use the __Subscription__ entry to select the one you want to use.

    ![Cluster name and subscription selections](/scaling_r_to_big_data/media/clustername.png)

4. Select __Select Cluster Type__. On the __Cluster Type__ blade, select the following options:

    * __Cluster Type__: R Server on Spark
    
    * __Cluster Tier__: Premium

    Leave the other options at the default values, then use the __Select__ button to save the cluster type.
    
    ![Cluster type blade screenshot](/scaling_r_to_big_data/media/clustertypeconfig.png)
    
    > [AZURE.NOTE] You can also add R Server to other HDInsight cluster types (such as Hadoop or HBase,) by selecting the cluster type, and then selecting __Premium__.

5. Select **Resource Group** to see a list of existing resource groups and then select the one to create the cluster in. Or, you can select **Create New** and then enter the name of the new resource group. A green check will appear to indicate that the new group name is available.

    > [AZURE.NOTE] This entry will default to one of your existing resource groups, if any are available.
    
    Use the __Select__ button to save the resource group.

6. Select **Credentials**, then enter a **Cluster Login Username** and **Cluster Login Password**.

    Enter an __SSH Username__ and select __Password__, then enter the __SSH Password__ to configure the SSH account. SSH is used to remotely connect to the cluster using a Secure Shell (SSH) client.
    
    Use the __Select__ button to save the credentials.
    
    ![Credentials blade](/scaling_r_to_big_data/media/clustercredentials.png)

7. Select **Data Source** to select a data source for the cluster. Either select an existing storage account by selecting __Select storage account__ and then selecting the account, or create a new account using the __New__ link in the __Select storage account__ section.

    If you select __New__, you must enter a name for the new storage account. A green check will appear if the name is accepted.

    The __Default Container__ will default to the name of the cluster. Leave this as the value.
    
    Select __Location__ to select the region to create the storage account in.
    
    > [AZURE.IMPORTANT] Selecting the location for the default data source will also set the location of the HDInsight cluster. The cluster and default data source must be located in the same region.

    Use the **Select** button to save the data source configuration.
    
    ![Data source blade](/scaling_r_to_big_data/media/datastore.png)

8. Select **Node Pricing Tiers** to display information about the nodes that will be created for this cluster. Unless you know that you'll need a larger cluster, leave the number of worker nodes at the default of `4`. The estimated cost of the cluster will be shown within the blade.

    ![Node pricing tiers blade](/scaling_r_to_big_data/media/pricingtier.png)

    Use the **Select** button to save the node pricing configuration.
    
9. On the **New HDInsight Cluster** blade, make sure that **Pin to Startboard** is selected, and then select **Create**. This will create the cluster and add a tile for it to the Startboard of your Azure Portal. The icon will indicate that the cluster is creating, and will change to display the HDInsight icon once creation has completed.

    | While creating | Creation complete |
    | ------------------ | --------------------- |
    | ![Creating indicator on startboard](/scaling_r_to_big_data/media/provisioning.png) | ![Created cluster tile](/scaling_r_to_big_data/media/provisioned.png) |

    > [AZURE.NOTE] It will take some time for the cluster to be created, usually around 15~40 minutes. Use the tile on the Startboard, or the **Notifications** entry on the left of the page to check on the creation process.
