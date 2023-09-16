# Mertin et al. (2017) simulation
import numpy as np
from dataclasses import dataclass

@dataclass
class Result:
    phenotype: np.ndarray
    site_id: np.ndarray
    causal_allele: np.ndarray
    effect_size: np.ndarray
    allele_frequency: np.ndarray    


def matrix(ts, h2, ncausal, random_seed):
    
    rng = np.random.default_rng(random_seed)
    
    causal_site_index = np.linspace(0, ts.num_sites-1, ncausal, dtype=int)
    
    allele_freq = np.zeros(ncausal, dtype=float)
    effect_size = np.zeros(ncausal, dtype=float)
    causal_allele = np.zeros(ncausal, dtype=object)
    
    nhaps = ts.num_samples

    prs_haps = np.zeros(nhaps) #score for each haplotype
    i = 0
    for variant in ts.variants():
        if variant.index in causal_site_index:
            sim_effect_size = np.random.normal(loc=0,scale=h2/ncausal)
            effect_size[i] = sim_effect_size
            causal_allele_index = rng.integers(low=1, high=len(variant.alleles))
            allele = variant.alleles[causal_allele_index]
            causal_allele[i] = allele
            genotype = np.array([1 if i == causal_allele_index else 0 for i in variant.genotypes])
            prs_haps += genotype * sim_effect_size
            allele_freq[i] = np.sum(genotype) / len(genotype)
            i += 1

    env_effect = rng.normal(loc=0,scale=1-h2, size=nhaps)
    prs_norm = (prs_haps - np.mean(prs_haps)) / np.std(prs_haps)
    env_norm = (env_effect - np.mean(env_effect)) / np.std(env_effect)
    total_liability = np.sqrt(h2) * prs_norm + np.sqrt(1 - h2) * env_norm
    
    simulation_result = Result(phenotype = total_liability,
                                        site_id = causal_site_index,
                                       causal_allele = causal_allele,
                                       effect_size = effect_size,
                                       allele_frequency = allele_freq)
    
    return simulation_result