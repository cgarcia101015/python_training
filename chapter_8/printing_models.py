import printing_functions as pf


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs[:], completed_models)
# Using [:] you can call a functions using a copy of the list not the original
# print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
# show_completed_models(unprinted_designs)