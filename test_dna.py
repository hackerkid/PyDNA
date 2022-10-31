from pydna import DNA

def test_convert_to_rna():
    DNA("GATGGAACTTGACTACGTAAATT").convert_to_rna() == "GAUGGAACUUGACUACGUAAAUU"