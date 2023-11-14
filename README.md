# python-app4-deploy
This repo is auto-generated through Glider. It has all the infrastructure required to provision a service in Ethos CaaS.Next.
Testing123456

> **_NOTE:_**  Please make sure that you have installed the [GitHub App](https://git.corp.adobe.com/github-apps/caas-gitops) on your Application and Deploy Repositories.

## Important Links

- Check the status of your Provisioning here: [Kibana Dashboard](https://ethos-kibana.ethos.corp.adobe.com:5601/app/dashboards#/view/0a9f9980-b4fd-11ec-9433-9b83da61415e?_a=(description:'This%20is%20dashboard%20to%20display%20provisioner%20events.',filters:!(('$state':(store:appState),meta:(alias:!n,controlledBy:'1649172517175',disabled:!f,index:'93a55740-b4f0-11ec-931c-e9c2e1d6feb7',key:eventData.data.payload.event_source_repository.keyword,negate:!f,params:(query:ethos-orca/python-app4-deploy),type:phrase),query:(match_phrase:(eventData.data.payload.event_source_repository.keyword:ethos-orca/python-app4-deploy)))),fullScreenMode:!t,options:(hidePanelTitles:!f,useMargins:!t),query:(language:kuery,query:''),tags:!(),timeRestore:!t,title:'Provisioner%20Events',viewMode:view))
- Argo Workfows : https://argo.ethos.corp.adobe.com
- Argo CD: https://argocd.ethos.corp.adobe.com
- [Link to Troubleshooting Guide](https://wiki.corp.adobe.com/display/ethos/Ethos+Troubleshooting+-+CaaS.next) : Use this to self resolve any issue before filing an [EON](https://jira.corp.adobe.com/secure/CreateIssueDetails!init.jspa?pid=31905&issuetype=11901&components=170501&priority=8&description=zerobin).


## Ethos K8S helm charts

Ethos has defined reusable templates for K8s objects to create a CaaS.Next Service. We release them in artifactory. You can checkout out the versions of our releases [here](https://git.corp.adobe.com/adobe-platform/ethos-k8s-helm-templates/releases)

## Folder Structure

```
├── argo
│   ├── Chart.yaml
│   ├── templates/
│   ├── values.yaml
└── k8s
    └── helm
        ├── Dev
        │   ├── va6
        │   │   ├── Chart.yaml
        │   │   └── values.yaml
        │   └── values.yaml
        └── values.yaml
```
- `argo`: This folder contains the workflow helm templates.
    - `values.yaml`: This file defines the attributes for the workflows.
- `k8s/helm`: This folder contains the helm templates for the K8s objects. 
    - `Chart.yaml` : This file defines the charts which will be used as dependencies.
    - `values.yaml`: This file defines the service level attributes for your service which can be overrided at the environment and region level if requried. Ethos recommendation is to specify all the attributes (needed for the service) in service level values.yaml of the repository.
    - `<environment>/values.yaml`:  This file defines the common attributes for an environment.
    - `<environment>/<region>/values.yaml`: This file defines the common attributes for a region.
 
    - 

