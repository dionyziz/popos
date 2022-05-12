from network import send, receive
from hash import H
from math import log, floor
from genesis import pk_0
from merkle import merkle_verify

def build_handover(C):
  return d

def build_tree(d, p=''):
  return T

def get_root(T):
  return T['']

def prover(V, C):
  d = build_handover(C)
  T = build_tree(d)
  pi = get_root(T)
  V.send({
    'root': pi,
    'n': len(d)
  })

def verifier(provers):
  proofs = []
  for i, prover in enumerate(provers):
    root, n = prover.recv()
    proofs.push({
      'root': root,
      'n': n,
      'party': prover
    })
  champion = proofs.pop() # tentative champion
  while len(proofs) > 0:
    competitor = proofs.pop()
    if bisect(champion, competitor):
      champion = competitor
  return champion['root']

def bisect(champion, competitor):
  B = ''

  def challenge(subtree_root, n, defender, attacker):
    nonlocal B

    if n == 0:
      value = defender.recv()
      if H(value) != root:
        return True
      if B == n:
        pk = value
      else:
        pk, sigma = value
      if B == 0:
        if pk != pk_0:
          return True
      else:
        prev_node, proof_of_inclusion = defender.recv()
        if not merkle_verify(prev_node, B - 1, proof_of_inclusion, root):
          return True

    children = defender.recv()
    if H(children) != subtree_root:
      return True
    attacker.send(children)
    direction = attacker.recv()
    B += direction
    defender.send(direction)
    left_size = 2**floor(log(n - 1, 2))
    if direction == 0:
      n = left_size
    else:
      n = n - left_size
    return challenge(children[direction], n, defender, attacker)

  if champion.n >= competitor.n:
    if challenge(champion.root, champion.n, champion.party, competitor.party):
      return competitor
  if champion.n <= competitor.n:
    if challenge(competitor.root, competitor.n, competitor.party, champion.party):
      return champion
  if champion.n >= competitor.n:
    return champion
  return competitor
