import pytest
import numpy as np
import networkx as nx
from molecool.bitstring import BitString
from molecool.ising import IsingHamiltonian

def make_test_graph():
    G = nx.Graph()
    G.add_nodes_from([0, 1])
    G.add_edge(0, 1, weight=1.0)
    return G

def test_init():
    G = make_test_graph()
    ham = IsingHamiltonian(G)
    assert ham.length == 2
    assert np.all(ham.mus == 0)

def test_energy():
    G = make_test_graph()
    ham = IsingHamiltonian(G)
    bs = BitString(2)
    bs.set_integer_config(0)
    energy = ham.energy(bs)
    assert np.isclose(energy, 1.0)

    bs.set_integer_config(3)
    energy2 = ham.energy(bs)
    assert np.isclose(energy2, 1.0)

def test_set_mu():
    G = make_test_graph()
    ham = IsingHamiltonian(G)
    mus = np.array([0.5, -0.5])
    ham.set_mu(mus)
    assert np.all(ham.mus == mus)

def test_compute_average_values():
    G = make_test_graph()
    ham = IsingHamiltonian(G)
    ham.set_mu(np.array([0.1, -0.1]))
    E, M, HC, MS = ham.compute_average_values(T=1.0)
    assert np.isfinite(E)
    assert np.isfinite(M)
    assert np.isfinite(HC)
    assert np.isfinite(MS)