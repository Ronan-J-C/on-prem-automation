import os
import yaml

service_types=['ClusterIP', 'NodePort', 'LoadBalancer', 'ExternalName']

deploy_types=['Deployment', 'ReplicaSet', 'StatefulSet', 'DaemonSet']
# https://medium.com/devops-mojo/kubernetes-service-types-overview-introduction-to-k8s-service-types-what-are-types-of-kubernetes-services-ea6db72c3f8c

REPO_PATH='/Users/ronancunningham/repos/kots/harness/base/harness'

REPO_PATH='/Users/ronancunningham/repos/on-prem-automation/opa/Policy Mgmt/Manifests/Files/templates'




def show_containers_info(doc):

    # print('YOYOYO')
    # print(doc)
    # print('YOYOYO')


                                # print(doc['spec'])

    init_containers=[]
    containers=[]

    if 'initContainers' in doc['spec']['template']['spec']:
        init_containers=doc['spec']['template']['spec']['initContainers']
    if init_containers:
        init_images=[x['image']for x in init_containers]
        print('init_containers')
        print(len(init_containers))
        print(init_images)
        # print(init_containers)
    else:
        print('NO init containers')

    if 'containers' in doc['spec']['template']['spec']:       
        containers=doc['spec']['template']['spec']['containers']
    if containers:
        print('containers')
        print(len(containers))
        images=[x['image']for x in containers]
        print(images)

        # print(containers)
    else:
        print('NO containers')
    print('\n','\n')


def explore_stateful_set(doc):
    init_containers=[]
    containers=[]

    volume_claim_templates=doc['spec']['volumeClaimTemplates']
    if volume_claim_templates:
        print('VOLUMECLAIMTEMPLATES')
        for vct in volume_claim_templates:
            print(' Name={}'.format(vct['metadata']['name']))

    volumes=doc['spec']['template']['spec']['volumes']
    if volumes:
        print('VOLUMES')
        for v in volumes:
            print(' Name={}'.format(v['name']))

    if 'initContainers' in doc['spec']['template']['spec']:
        init_containers=doc['spec']['template']['spec']['initContainers']
    if init_containers:
        print('\nINIT CONTAINERS:')
        for init in init_containers:
            name=init['name']
            image=init['image']
            volume_mounts=init['volumeMounts']

            print(name,image)
            if volume_mounts:

                print('Volume Mounts')

                for mount in volume_mounts:
                    print(mount)
            else:
                print('no volume mounts')

        # print(init_containers)
    else:
        print('NO init containers')

    print('\n')
def list_files():


    for root, dirs, files in os.walk(REPO_PATH):

        for file in files:

            # if 'mongodb' in file:
            if '.yaml' in file:
                # print(file)
                fqp = os.path.join(root,file)
                # print(fqp)
                opened = open(os.path.join(root,file), "r")
                # print(opened)
                documents = yaml.load_all(opened, yaml.FullLoader)

                for doc in documents:



                    if doc:
                        kind=doc['kind']
                        # if kind in deploy_types:
                        #     print(kind,file)
                        #     show_containers_info(doc)

                        if kind == 'StatefulSet':
                            print('\n')
                            print(kind,file)
                            explore_stateful_set(doc)



                    

list_files()