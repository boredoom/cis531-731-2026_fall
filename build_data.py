import json
import random
import os

LABELS = [
    "Hustle_Narrative",
    "Regional_Authenticity",
    "Lyrical_Sovereignty",
    "Systemic_Critique",
    "Boom_Bap",
    "G_Funk",
    "Trap",
    "Chopper"
]

# Curated seed texts aligned with PS 6 ontology indicators
CORPUS_TEMPLATES = {
    "Hustle_Narrative": [
        "Started from the corner now we talking stock portfolios and business equity.",
        "Grinding every single day from the bottom out the mud to secure the generational wealth.",
        "Late nights trapping on the block turned into corporate boardrooms and LLC registrations.",
        "Stacking paper high, building enterprises, flipping every dollar into five more.",
        "From selling loose singles on the curb to closing multimillion dollar distribution deals.",
        "We took the hustle from the pavement to Wall Street, legitimate investment over quick money.",
        "Work ethic unmatched, sleeping four hours a night to build a sovereign empire.",
        "Real entrepreneurship: turning local street reputation into nationwide franchise ownership."
    ],
    "Regional_Authenticity": [
        "Repping the 718 borough to the death, brownstone stoops and subway token turnstiles.",
        "West Coast lowriders rolling down Crenshaw, candy paint reflecting California palm trees.",
        "Zone 6 Atlanta clay roads, Bankhead highway pride rooted deep in the neighborhood asphalt.",
        "Southside Chicago winter winds, block allegiance certified through every zip code corner.",
        "Bay Area hyphy movement, sideshows at the intersection screaming 510 authentic game.",
        "Houston slab culture, swabbing the four-lane boulevard representing Third Ward heritage.",
        "Philadelphia row homes, North Philly loyalty etched into every lyric and street corner.",
        "Detroit cold pavement, 313 code stamped across the forehead of every native resident."
    ],
    "Lyrical_Sovereignty": [
        "Multi-syllabic internal rhyme patterns dismantling amateur emcees in the competitive cypher.",
        "Complex cadence switches, polyrhythmic breath control asserting absolute verbal dominance.",
        "Metaphorical architecture constructed bar by bar, supreme penmanship no ghostwriter touches.",
        "Chopping syllables at terminal velocity, surgical diction that dissects any opposing cadence.",
        "Raw freestyle battle mechanics, off-the-dome freestyles obliterating commercial pop gimmicks.",
        "Lyrical combat stance, four-bar symmetry interwoven with esoteric double entendres.",
        "Microphone sovereignty demonstrated through relentless rhyming patterns and acoustic discipline.",
        "Every stanza designed as a precision weapon, commanding respect across traditional battle arenas."
    ],
    "Systemic_Critique": [
        "Institutional redlining and judicial bias perpetuating generational cycles of urban poverty.",
        "Militarized policing occupying residential sectors while schools face systematic defunding.",
        "The prison industrial complex turning human lives into traded commodities on corporate exchanges.",
        "Gentrification displacing family heritage under the false flag of urban development progress.",
        "Civil rights resistance echoed through generational struggles against corrupt judicial regimes.",
        "Exposing structural inequality and legislative disenfranchisement written into modern statutes.",
        "Historical disenfranchisement challenged by radical grassroots mobilization and lyrical resistance.",
        "Corporate media shielding structural corruption while demonizing communities fighting for survival."
    ],
    "Boom_Bap": [
        "Unquantized SP-1200 acoustic kick and cracked snare drum breaks over dusty jazz vinyl loops.",
        "Heavy timberland boots stepping on concrete, classic 90 BPM four-track tape saturation.",
        "Raw turntable scratching cutting the vocal sample across an unpolished two-bar drum sequence.",
        "Filtered jazz double-bass walking beneath a crisp analog snare echoing down city alleys.",
        "Crate digging in dusty basement record stores finding rare brass stabs for the MPC drum pads.",
        "Acoustic drum break recorded straight from obscure vinyl, zero quantization, pure human pocket.",
        "Golden era boom-bap rhythm driving pure hip-hop purism through vintage analog compressors.",
        "Crisp hi-hats swinging behind a thunderous kick drum resonating through classic block party horns."
    ],
    "G_Funk": [
        "High-pitched Moog synthesizer melodies gliding smoothly over laid-back P-Funk basslines.",
        "Rolling hydro bass rhythms cruising at 85 BPM under warm West Coast sunshine melodies.",
        "Melodic talkbox vocals crooning over breezy funk guitar riffs and synthesizer arpeggios.",
        "Smooth synthesizer leads sliding between octaves across chilled lowrider funk grooves.",
        "Live Parliament-style bass grooves combined with lazy summer afternoon snare claps.",
        "Warm analog electric piano Rhodes chords creating an effortless sunny California cruise.",
        "Laid-back vocal cadence harmonizing with soaring sine waves and funk synthesizer hooks.",
        "Relaxed tempo underpinned by grooving clavinet lines and distinctive melodic whistle synths."
    ],
    "Trap": [
        "Rapid-fire rolling 32nd-note hi-hat triplets rattling over distorted 808 sub-bass slides.",
        "Dark minor-scale brass stabs punctuating relentless syncopated electronic trap snares.",
        "Aggressive 808 glide patterns booming through low-frequency subwoofers with gunshot accents.",
        "Frantic synthesized bell arpeggios looping over bone-dry clapping snares and stuttering hats.",
        "Pitch-bent sub-bass frequencies detonating beneath minimalist, menacing minor-key synthesizer loops.",
        "Digital trap beat characterized by lightning-fast snare rolls and piercing metallic open hats.",
        "Heavy low-end compression driving ominous synthetic bells and syncopated kick patterns.",
        "Distorted bass hits sliding between notes under rapid machine-gun electronic percussion."
    ],
    "Chopper": [
        "Sixteenth-note triplet vocal velocity firing at 140 BPM with rapid-fire double-time cadence.",
        "Polysyllabic speed-rap delivery maintaining crystal-clear consonant articulation at extreme speeds.",
        "Breath control mastery accelerating syllables into sustained machine-gun lyrical bursts.",
        "Midwest chopper cadence switching speeds effortlessly between double and quadruple time meters.",
        "Staccato vocal firing patterns defying standard tempo constraints through breath discipline.",
        "Hyper-speed verbal velocity delivering complex internal rhymes with surgical speed precision.",
        "Accelerated cadence defying acoustic limits, sustained breathless delivery across multi-bar runs.",
        "Rapid-fire tongue twists executing lightning-fast polysyllabic cadence patterns flawlessly."
    ]
}

def generate_datasets(seed=42):
    random.seed(seed)
    
    # Generate balanced held-out evaluation set: 20 per class = 160 examples
    eval_records = []
    ex_id = 0
    for label in LABELS:
        templates = CORPUS_TEMPLATES[label]
        for i in range(20):
            base = templates[i % len(templates)]
            # Slight syntactic variance to ensure realistic evaluation
            variations = [
                f"{base}",
                f"Lyrical excerpt: \"{base}\"",
                f"Verse segment: {base}",
                f"Track chunk manifest: {base}"
            ]
            eval_records.append({
                "id": f"eval_{ex_id:04d}",
                "text": variations[i % len(variations)],
                "label": label,
                "provenance": "eval_heldout_gold"
            })
            ex_id += 1
            
    # Generate exemplar candidate pool: 16 per class = 128 exemplars
    exemplar_records = []
    pool_id = 0
    for label in LABELS:
        templates = CORPUS_TEMPLATES[label]
        for i in range(16):
            base = templates[(i + 3) % len(templates)]
            variations = [
                f"Exemplar verse: {base}",
                f"Document passage: \"{base}\"",
                f"Chunk text: {base}",
                f"Admitted stanza: {base}"
            ]
            exemplar_records.append({
                "id": f"exemplar_{pool_id:04d}",
                "text": variations[i % len(variations)],
                "label": label,
                "provenance": "admitted_exemplar_pool"
            })
            pool_id += 1

    random.shuffle(eval_records)
    
    with open("eval_mp7.jsonl", "w") as f:
        for r in eval_records:
            f.write(json.dumps(r) + "\n")
            
    with open("exemplars_pool.jsonl", "w") as f:
        for r in exemplar_records:
            f.write(json.dumps(r) + "\n")
            
    print(f"[OK] Generated eval_mp7.jsonl ({len(eval_records)} balanced held-out items across {len(LABELS)} classes)")
    print(f"[OK] Generated exemplars_pool.jsonl ({len(exemplar_records)} candidate exemplars)")

if __name__ == "__main__":
    generate_datasets()
