#
#
# Baby runner

OBJECTIVE = "Get the time of day"

llm = OpenAI (temperature=0 )

# Logging of LLMChains
verbose=False

# If None, will keep on going forever
max_iterations: Optional[ int ] = 3
baby_agi = BabyAGI.from_llm(
    llm=llm,
    vectorstore=vectorstore,
    verbose=verbose,
    max_iterations=max_iterations
)

baby_agi({"objective": OBJECTIVE})


