# TO-DO: Containerize to microservice
import numpy as np

# Takes 
# Requires: Aerodynamic coefficients
# Required by: Equations of motion and nonlinear motion
# Outputs: Aerodynamic forces and moments
class Gravitation():
  def __init__(self, metadata_distributor):
    self.metadata_distributor = metadata_distributor
    self.eta = self.metadata_distributor.get_var('eta')
    self.lamb = self.metadata_distributor.get_var('lamb')
    self.h = self.metadata_distributor.get_var('h')
  
  def get_gravity(self):
    g_z = 9.7803267714 * (1+0.00193185138639*np.sin(self.eta)**2)/ \
        (1 - 0.00669437999013*np.sin(self.eta)**2)
    g_xyz = np.array([0,0,g_z])
    self.metadata_distributor.set({'g_xyz': g_xyz})
    return g_xyz
  
  def get_apparent_gravity(self):
    # gets gravity based on external database giving
    # longitude, latitude, altitude
    return
