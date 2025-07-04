"""
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService

token = "9GnuRC52XrVFyby469dONa00TKhpl5X_6oMFmqw5UTrd"
instance = "crn:v1:bluemix:public:quantum-computing:us-east:a/07c3187e648c42cc89d6cfc1c2c36b9b:02cf699e-389f-46b2-936b-be27c8d9b1b1::"

QiskitRuntimeService.save_account (
    token = token,
    instance= instance,
    set_as_default= True
)

service = QiskitRuntimeService()
print(service.backends())
# Create Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Simulate the circuit using run() directly
backend = Aer.get_backend("qasm_simulator")
result = backend.run(qc).result()

print("Result:", result.get_counts())
*/
"""