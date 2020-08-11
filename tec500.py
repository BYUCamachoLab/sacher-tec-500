import pyvisa

try:
    import tec500_methods
except ImportError:
    print(f"Failed to import tec500_methods. Run '{__file__}' directly to generate.")

resource_manager = pyvisa.ResourceManager()

class TEC500():
    def __init__(self, address):
        self.device = resource_manager.open_resource(address)

    def __get_response(self):
        # 2 Ways to read the responses.
        # Method 1: Read responses into list until exception occurs.
        # Method 2: Check/track state of echo & command responses and filter those out.
        
        # Method 1 example.
        responses = list()
        try:
            while True:
                responses.append(self.device.read())
        except Exception:
            # TODO: Use the correct Exception type and verify it.
            # Exception will be thrown when all responses are read.
            pass
        return responses[-1] # Return the last response.


    def __send_command(self, command):
        self.device.write(command)
        return self.__get_response()
        

# ------------------------------------------------------------- #
# METHOD GENERATOR
# ------------------------------------------------------------- #

method_template = """
def {methodname}(self, args):
    {docstring}
    return self.__send_command(f"{Syntax}")
TEC500.{methodname} = {methodname}
"""

def generate_methods():
    """Generate methods based on the command reference."""
    import csv

    with open ("tec500_methods.py", "w+") as extensions:
        extensions.write("from tec500 import TEC500\n\n")
        with open("command_reference.csv", newline='') as command_docs:
            reader = csv.DictReader(command_docs)
            for docs in reader:
                # HACK: Generate method names for testing.
                docs["methodname"] = docs["Name"].replace(" ", "_").replace("(", "").replace(")","").replace("-", "_")
                docs["docstring"] = f'"""{docs["Description"]}"""'

                if docs["Name"] == "":
                    continue
                extensions.write(method_template.format(**docs))

if __name__ == "__main__":
    generate_methods()