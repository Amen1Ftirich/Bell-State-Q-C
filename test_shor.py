"""
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_ibm_runtime import QiskitRuntimeService

token = "NAHUH"
instance = "nah"

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
