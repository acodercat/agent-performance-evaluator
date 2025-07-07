def biological_calc_biomass(energy, efficiency=0.1):
	"""
	Calculate the biomass from the energy given the energy conversion efficiency.    
	Parameters:
	energy: The total energy produced.
	efficiency: The conversion efficiency, default value is 10%.

	"""
	pass

def biological_calc_energy(mols, substance, joules_per_mol=2800):
	"""
	Calculate energy from amount of substance based on its molecular composition.    
	Parameters:
	mols: Amount of substance in moles.
	substance: The chemical formula of the substance.
	joules_per_mol: The energy produced or required for the reaction, default value for glucose is 2800 kJ/mol

	"""
	pass

def physical_calc_work(energy, distance):
	"""
	Calculate the work from energy.    
	Parameters:
	energy: The total energy produced.
	distance: The distance over which the work is done.

	"""
	pass

tools = [biological_calc_biomass, biological_calc_energy, physical_calc_work]
