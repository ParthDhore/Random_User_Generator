from controller.generate import Random_user
def initialize_routes(api):
    api.add_resource(Random_user,'/generate_user')