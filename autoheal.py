import docker

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

for event in client.events(decode=True):
    if event['Type'] == 'container' and event['status'] == 'health_status: unhealthy':
        print(event)
        print("The container is detected to be unhealthy, try to restart")
        container = client.containers.get(event['id'])
        container.restart()