from . import fuckbrain
from ipykernel.kernelbase import Kernel


class FuckbrainKernel(Kernel):

    implementation = "Fuckbrain"
    implementation_version = "0.1"
    language_info = {
        "name": "text",
        "mimetype": "text/plain",
    }

    banner = "Fuckbrain - The reverse brainfucking"

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):

        if code.startswith("%%beautiful\n"):
            output = fuckbrain.generate_beautified(code[12:])
        else:
            output = fuckbrain.generate(code)

        if not silent:
            stream_content = {
                "data": {
                    "text/plain": output
                },
                "execution_count": self.execution_count,
                "metadata": {}
            }
            self.send_response(self.iopub_socket, "execute_result", stream_content)

        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {}
        }

if __name__ == "__main__":
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=FuckbrainKernel)
