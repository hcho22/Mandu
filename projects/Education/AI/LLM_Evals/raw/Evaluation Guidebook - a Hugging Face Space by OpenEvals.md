---
title: Evaluation Guidebook - a Hugging Face Space by OpenEvals
source: https://huggingface.co/spaces/OpenEvals/evaluation-guidebook#generative-evaluations
author:
published:
created: 2026-06-15
description: View an interactive chart that follows the top scores of major LLM benchmarks across Hugging Face leaderboards over the years. The page needs no input—just open it to see record‑setting lines, aver...
tags:
---
# The LLM Evaluation Guidebook

### The benchmark lifecycle

MUSR, BBH, Winogrande, TruthfulQA, HellaSwag

About this chart

This visualization tracks the evolution of top benchmark scores over time across 3 leaderboards managed by Hugging Face through the years: the Open LLM Leaderboard 1, 2, and the GAIA leaderboard. The step-like lines represent the progression of maximum scores achieved for each benchmark, with circular markers indicating when a new record was set. It illustrates a phenomenon known as saturation.

The gray scatter plot in the background shows the average scores of all evaluated models for a given leaderboard at a given time, and allows to follow the trend of submission for each leaderboard.

Benchmarks are grouped by category (Reasoning & Commonsense, Knowledge, Math, Agentic, and Instruction following), with each group sharing a color family.

All the things you could want to know about LLM evaluation based on our experience scoring 15000 models over 3 years

### Authors

- [Clémentine Fourrier](https://huggingface.co/clefourrier), 
- [Thibaud Frere](https://huggingface.co/tfrere), 
- [Guilherme Penedo](https://huggingface.co/guipenedo), 
- [Thomas Wolf](https://huggingface.co/thomwolf)

### Affiliation

[Hugging Face](https://huggingface.co)

### Published

Dec. 03, 2025

## [What is model evaluation about?](https://openevals-evaluation-guidebook.hf.space/#what-is-model-evaluation-about)

As you navigate the world of LLMs — whether you’re training or fine-tuning your own models, selecting one for your application, or trying to understand the state of the field — there is one question you have likely stumbled upon:

> How can one know if a model is _good_?

The answer is (surprisingly given the blog topic) evaluation! It’s everywhere: leaderboards ranking models, benchmarks claiming to measure _reasoning_, _knowledge_, _coding abilities_ or _math performance_, papers announcing new state-of-the-art results…

But what is evaluation, really? And what can it really tell you?

This guide is here to help you understand it all: what evaluation can and cannot do, when to trust different approaches (what their limitations and biases are too!), how to select benchmarks when evaluating a model (and which ones are relevant in 2025), and how to design your own evaluation, if you so want.

Through the guide, we’ll also highlight common pitfalls, tips and tricks from the Open Evals team, and hopefully help you learn how to think critically about the claims made from evaluation results.

In this guide, we focus on evaluations for language (mostly natural language), but many principles also apply to other modalities

Before we dive into the details, let’s quickly look at why people do evaluation, as who you are and what you are working on will determine which evaluations you need to use.

### [The model builder perspective: Am I building a strong model?](https://openevals-evaluation-guidebook.hf.space/#the-model-builder-perspective-am-i-building-a-strong-model)

If you are a researcher or engineer creating a new model, your goal is likely to build a strong model that performs well on a set of tasks. For a base model (training from scratch), you want the model to do well on a general tasks, measuring a variety of different capabilities. If you are post-training a base model for a specific use case, you probably care more about the performance on that specific task. The way you measure performance, in either case, is through evaluations.

As you experiment with different architectures, data mixtures, and training recipes, you want to make sure that your changes (choosing different training data, architecture, parameters, etc) have not “broken” the expected performance for a model of these properties, and possibly even improved it. The way you test for the impact of different design choices is through **ablations**: an ablation is an experiment where you typically train a model under a specific setup, evaluate it on your chosen set of tasks, and compare the results to a baseline model. Therefore, the choice of evaluation tasks is critical for ablations, as they determine what you will be optimizing for as you create your model.

Ablation example

Say you want to compare dataset A and dataset B (for example, Wikipedia vs Reddit) to see how they affect model performance. You train models under the same setups on each, then evaluate and compare the scores on benchmarks.

For base models, one would typically resort to selecting standard benchmark tasks used by other model builders (think the classic list of benchmarks that are always reported when a new model is released - we’ll have a look at those below). For a specific use case, you can either use existing evaluation tasks if they are available — and you likely will want to take a good look if they are not “standard” — or design your own (discussed below). As you will likely run a lot of ablations, you want the evaluation tasks to provide strong enough signal (and not just meaningless noisy results) and you want them to run cheaply and quickly, so that you can iterate fast. Through ablations, we are also able to predict the performance of bigger models based on the perfomance on smaller ones, using scaling laws.

Besides ablations for experiments, you will likely also want to run evaluations on intermediate checkpoints as your model is training, to ensure it is properly learning and improving at the different tasks, and does not start regressing due to spikes or other issues. Finally, you want to evaluate the final checkpoint so that you can announce that your model is SOTA when you release it.

Small caveat

Despite often grandiose claims, for any complex capability, we cannot at the moment just say “this model is the best at this”, but should instead say **“this model is the best on these samples for this specific task that we hope are a good proxy for this capability, without any guarantee”**.

(You can still claim you are SOTA, just keep the caveat in mind.)

### [The model user perspective: Which model is the best on <task>?](https://openevals-evaluation-guidebook.hf.space/#the-model-user-perspective-which-model-is-the-best-on-task)

You want to use a model someone else trained for your specific use case, without performing additional training, or maybe you will perform additional training and are looking for the best existing model to use as a base.

For common topics like math, code, or knowledge, there are likely several leaderboards comparing and ranking models using different datasets, and you usually just have to test the top contenders to find the best model for you (if they are not working for you, it’s unlikely the next best models will work).

You could want to run the evaluation and comparisons yourself (by reusing existing benchmarks) to get more details to analyse on the model successes and failures, which we will cover below.

In [their paper](https://arxiv.org/pdf/2404.02112) about lessons learned on benchmarking and dataset design from the ImageNet era, the authors argue that, since scores are susceptible to instability, the only robust way to evaluate models is through rankings, and more specifically by finding broad groups of evaluations which provide consistent and stable rankings. I believe looking for ranking stability is indeed an extremely interesting approach to model benchmarking, as we have shown that LLMs _scores_ on automated benchmarks are extremely susceptible to [minute changes in prompting](https://huggingface.co/blog/evaluation-structured-outputs), and that human evaluations are not more consistent - where _rankings_ are actually more stable when using robust evaluation methods.

Similarly to model builders hillclimbing a specific capability, for less common topics, you might need to think about designing your own evaluations, which is detailed in our last section.

🎯

Takeaways

- Model builder: You need fast, high-signal benchmarks that cover the domains/capabilities you care about and can be run repeatedly during ablations.
- Model user: You need benchmarks that match your specific use case, even if that means creating custom ones.

What about measuring AGI?

We are strongly missing any kind of good definitions and framework on what intelligence is for machine learning models, and how to evaluate it (though some people have tried, for example [Chollet](https://arxiv.org/abs/1911.01547) in 2019 and [Hendrycks et al](https://www.agidefinition.ai/paper.pdf) this year). Difficulty in defining intelligence is not a problem specific to machine learning! In human and animal studies, it is also quite hard to define, and metrics which try to provide precise scores (IQ and EQ for example) are hotly debated and controversial, with reason.

There are, however, some issues with focusing on intelligence as a target. 1) Intelligence tends to end up being a moving target, as any time we reach a capability which was thought to be human specific, we redefine the term. 2) Our current frameworks are made with the human (or animal) in mind, and will most likely not transfer well to models, as the underlying behaviors and assumptions are not the same. 3) It is kind of a useless target too - we should target making models good at specific, well defined, purposeful and useful tasks (think accounting, reporting, etc) instead of aiming for AGI for the sake of it.

## [LLM basics to understand evaluation](https://openevals-evaluation-guidebook.hf.space/#llm-basics-to-understand-evaluation)

Now that you have an idea of why evaluation is important to different people, let’s look at how we prompt models to get some answers out in order to evaluate them. You can skim this section if you have already done evaluation and mostly look for the notes and sidenotes.

In this section, we’ll look at two steps for models: how input is preprocessed to be given to the model (`tokenization`), and how the model generates a prediction from it (`inference`).

If you want to learn more about how to actually train a model, you should go read the [Smol Training Guidebook!](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook)

Input Text "Hello, world!" Tokenizer Split into tokens Tokens Hello , world ! [5425] [11] [1917] [0] Language Model Process & Generate Output / Prediction

### [Tokenization](https://openevals-evaluation-guidebook.hf.space/#tokenization)

The input text (called a _prompt_ at inference) is first split into _tokens_, small units of texts (which can be one or several characters, up to the word level) each associated with a number. The whole range of tokens a model can parse is called its _vocabulary_.

#### [Basics of tokenization: Why and how do we tokenize text?](https://openevals-evaluation-guidebook.hf.space/#basics-of-tokenization-why-and-how-do-we-tokenize-text)

Since large language models are actually big mathematical functions, they eat numbers, not text.

Say you want to transform a sentence to numbers. You first need to decide how to cut your sentence into small pieces, then map every small piece to a number; this is _tokenization_.

In the past, people would try to map each character of a text with its index in a alphabet (`a` -> 1, `b` -> 2, etc) which is called _character based tokenization_ (you split between characters). On the other end of the spectrum, people also tried to map each word with its index in a dictionary (`a` -> 1, `aardvark` -> 2, `ab` -> 3, etc) which is called _word based tokenization_ (you split on spaces, if your language has spaces - if not, it’s a bit harder).

Both these methods share a strong limitation: they remove information from the input text. They erase semantic connections that you can see from word shape (ex: `dis similar`, `similar`, `similar ity`, `similar ly`), information we would like our model to retain, so it connects related words together. (Plus, what happens if you suddenly have a completely new word in input? It gets no number, and your model can’t process it 😔 )

Some people therefore had the idea to cut words into sub-words, and assign index to these sub-words (`dis`, `similar`, `ity`, `ly`)!

This was initially done using morpho-syntactic rules (_morpho-syntax_ is like the grammar of word creation). Now most people use byte pair encoding (BPE), a smart statistical method to create the sub-words automatically depending on their frequency in a reference text.

So as a summary: tokenization is a way to map small units of texts (which can be one or several characters, up to the word level) to numbers (similar to an index). When you want to process text, your input text (called a _prompt_ at inference) is split into these _tokens_ by a tokenizer. The whole range of tokens a model or tokenizer can parse is called its _vocabulary_.

📚

Going further: Understanding tokenization

- ⭐ [Explanation of different tokenization methods in the 🤗 NLP Course](https://huggingface.co/learn/nlp-course/en/chapter2/4)
- ⭐ [Conceptual guide about tokenization in the 🤗 doc](https://huggingface.co/docs/transformers/en/tokenizer_summary)
- [Course by Jurafsky on tokenization (and other things)](https://web.stanford.edu/~jurafsky/slp3/2.pdf) - skip to 2.5 and 2.6

📚

Going further: Byte Pair Encoding

I would strongly recommend reading a longer explanation on how BPE works, as it’s really a base of modern LLMs.

- ⭐ [Explanation of BPE in the 🤗 NLP Course](https://huggingface.co/learn/nlp-course/en/chapter6/5)
- [BPE Paper (for text, as the method existed before in other fields)](https://aclanthology.org/P16-1162/)

Building a tokenizer requires making more choices than one would expect. For example, to tokenize numbers, you don’t want to use a basic BPE, but do you only index 0 to 9, and assume all other numbers will be compositions of digits? Do you want to store numbers up to, say, one billion, individually?

Current well known models display a range of approaches to this, but it’s unclear what works better to allow mathematical reasoning. This will affect some mathematical evaluation (and is the reason why almost no evaluation is pure arithmetics).

📚

Going further: Tokenizing numbers

- ⭐ [A nice visual demo by Yennie Jun of how tokenizers of Anthropic, Meta, OpenAI, and Mistral models split numbers](https://www.artfish.ai/p/how-would-you-tokenize-or-break-down)
- [Small history by Beren Millidge of the evolution of number tokenization through the years](https://www.beren.io/2024-05-11-Integer-tokenization-is-now-much-less-insane/)

#### [How tokenization can mess up your evaluation](https://openevals-evaluation-guidebook.hf.space/#how-tokenization-can-mess-up-your-evaluation)

**Managing fine-tuned models, system prompts and chat templates**

Pre-2022, models used to simply be pretrained: text in, text out, nothing else. Then, we got instruction tuning and chat models in 2023, and in 2025 reasoning models. This means that we went from using raw text to using more and more formatting.

Raw Text Early Models (before 2022) Evolution Chat Templates (in JSON) Chat Models (2022-2025) Evolution JSON + XML Reasoning Models (2025+) • Simple prompts • Generally no structure • Completion-based • Role separation • Chat/Turn-based • Chat/Turn-based with added tags for control Before 2022 2022-2025 2025+

This means a number of models are going to perform terribly if you do not make sure to:

1. respect the format the model expectes
2. adds a system prompt at the very beginning of inference if your model requires one
3. remove the thinking trace from reasoning models answers before processing them (you can usually regex to remove what’s between the `<think>` tags)

⚡

Critical: Chat templates and tokenization

![Spacing, tokenization and template](https://openevals-evaluation-guidebook.hf.space/_astro/chat-templates-and-tokenisation.BfnD-hXa_1H9miV.webp)

Different tokenizers behave differently with spacing and special tokens. See this [visualization](https://x.com/danielhanchen/status/1796952220619157694) showing how spacing, tokenization, and templates interact. Never assume tokenizers behave identically!

**Paying attention to start and end of sentence tokens**

Some pretrained models, like the `Gemma` ones, are extremely sensitive to the [inclusion of start of sentence tokens](https://github.com/EleutherAI/lm-evaluation-harness/pull/1465) at inference. You might need to do a couple of experiments to see if that happens for you, and add these tokens manually when evaluating if they are not in your dataset.

You can also encounter some issues where your model won’t stop on an end of sentence token like you would expect. Code models usually have been trained with `\n\t` as a single token. This means that when generating text, they will often generate `\n\t` in one step. A task which defines `\n` as an end of sentence token (= to stop the generation) will let the model continue generating after a `\n\t`, if predicted as one token, since it’s not the same as `\n`. But you would actually still want the model to stop. In these cases, you either need to update your end of sentence tokens, or define a mechanism to backtrack on the character representation of the latest tokens to stop (and cut) the generation a posteriori.

**Multilinguality and tokenization**

When looking at multilingual evaluations, you’ll encounter two issues.

First, as some languages do not always use spacing as a word separator (Korean, Thai, Japanese, Chinese, to cite a few), they will require language specific tokenizers to be split properly, else it will affect their scores on metrics such as [BLEU](https://github.com/EleutherAI/lm-evaluation-harness/issues/212), F1 scores, etc.

Then, tokenizers in general might be unfair to non-English languages. When training a BPE tokenizer, you use data from the different languages you want to cover, but most of the time, though, this data is unbalanced between languages (with, for example, an order of magnitude more English than Thai, or Burmese). Since BPE tokenizers create their vocabulary tokens based on the most frequent words seen, most of the long tokens will be English words - and most of the words from the less frequent languages will only be split at the character level. This effect leads to an unfairness in multilingual tokenization: some (less frequent, or _lower-resourced_) languages require orders of magnitude more tokens to generate a sentence of equivalent length as English.

Very nice demo by Yennie Jun on tokenization issues across languages

If you are in this case, the number of tokens that the model is allowed to generate for an evaluation should also be language dependent, as not all languages are tokenized in similar amount of tokens.

📚

Going further: Language and tokenization

- ⭐ [A beautiful breakdown and demo by Yennie Jun on tokenization issues across languages](https://www.artfish.ai/p/all-languages-are-not-created-tokenized): The breakdown in itself is very clear, and the embedded space comes from her work.
- ⭐ [A demo by Aleksandar Petrov on unfairness of tokenization](https://aleksandarpetrov.github.io/tokenization-fairness/): I recommend looking at `Compare tokenization of sentences` to get a feel for the differences in cost of inference depending on languages

### [Inference](https://openevals-evaluation-guidebook.hf.space/#inference)

Now that we know how to convert our input text into something the LLMs can parse, let’s look at how models process this text.

From this input text, the LLM generates a probability distribution of the most likely next tokens over all the vocabulary. To get a continued generation, we can take the most probable token (give or take some added randomness to get more interesting outputs) as the next one, then repeat the operation, using the new token as the end of the prompt, etc.

![LLM tokenization and prediction process](https://openevals-evaluation-guidebook.hf.space/_astro/llm_tk_1.BVI0TDSU_1F5u4t.webp)

🎯

Two main evaluation approaches

**Log-likelihood evaluations**: Given a prompt and one (or several) answers, what is probability of said answer(s) for my model?

**Generative evaluations**: Given a prompt, what text does my model generate?

Choice depends on your task (as we’ll see below) and on your model: most models under APIs do not return the logprobabilities, so you’ll need to use generative evaluations systematically to evaluate them.

#### [Log-likelihood evaluations](https://openevals-evaluation-guidebook.hf.space/#log-likelihood-evaluations)

For log-likelihood evaluations, we want the conditional probability of one or several choices given a prompt - in other terms, what is the likelihood to get a specific continuation given an input? So:

- we concatenate each choice with the prompt, and pass them to our LLM, which outputs the logits of each token depending on the previous ones
- we only keep the last logits (associated with the choice tokens), and apply a log softmax to get log-probabilities (where the range is `[-inf, 0]` instead of `[0-1]`)
- we then sum all individual tokens log probabilities to get the overall choice log probability
- we can finally apply a normalization based on choice length

![LLM log-likelihood evaluation process](https://openevals-evaluation-guidebook.hf.space/_astro/llm_logprob.C6BUmXKF_ZKqHgL.webp)

This allows us to apply one of the following metrics:

- get the preferred answer of a model among several choice, like in the above picture. (_However, this can advantage scores of models which would have, freely, generated something else, like `Zygote` in the picture._)
- test if a single choice has a probability above 0.5
- study model calibration. A well calibrated model is a model for which the correct answers have the highest probabilities.

To learn more about calibration, you can check [this paper](https://arxiv.org/abs/2207.05221) from Anthropic, on what it is, how to detect it, and how to train models to be well calibrated, and [this paper](https://arxiv.org/abs/2311.14648) on some possible limits of calibration).

A multiple choice question answer can be expressed as a free form generative evaluation too! For this reason, you’ll sometimes see a mention of the task **formulation**.

There are three common task formulations:

- **Multiple choice format (MCF)**: we compare the likelihood of choices indices, where choices are explicitly presented in the prompt and prefixed with A/B/C/D (as in MMLU)
- **Cloze formulation (CF)**: we compare the likelihood of different choices without providing them in the prompt
- **Freeform generation (FG)**: we evaluate the accuracy of greedy generation for a given prompt

FG requires substantial latent knowledge and is usually too difficult for models during short pre-training ablations. For this reason, we typically focus on multiple choice formulations (MCF or CF) when running small-scale ablations. However, for post-trained models, FG becomes the primary formulation since we’re evaluating whether the model can actually generate useful responses. However, research has also shown that models struggle with MCF early in training, only learning this skill after extensive training, making CF better for early signal. We thus recommend using CF for small ablations, and integrate MCF in the main run as it gives better mid-training signal once a model has passed a threshold to get sufficiently high signal-over-noise ratio for MCF. A quick note also that, to score a model’s answer in sequence likelihood evaluations like CF, we compute accuracy as the percentage of questions where the the correct answer has the highest log probability normalised by character/token count. This normalisation prevents a bias toward shorter answers.

The point at which MMLU MCF becomes non-random depends on the model size and training data. For a 7B transformer, the OLMES paper found the model starts showing non-random performance after 500B tokens. For 1.7B model, we found this happens after 6T tokens in SmolLM2.

[](https://github.com/EleutherAI/lm-evaluation-harness/pull/531#issuecomment-1595586257)

#### [Generative evaluations](https://openevals-evaluation-guidebook.hf.space/#generative-evaluations)

For a generative evaluation, we want the text generated by the model given an input prompt.

It is obtained in an auto-regressive way: we pass the prompt to the model, look at the most likely next token, select it as being the model’s “choice first token”, then repeat until we reach an end of generation condition (maximum length, special token to stop the generation, etc). All the tokens generated by the model are consider its answer to the prompt.

![LLM generative evaluation process](https://openevals-evaluation-guidebook.hf.space/_astro/llm_gen.DI9LEVxG_15bN7u.webp)

We can then compare this generation with references and score the distance between both (using either simple metrics like exact match, more complex metrics like BLEU, or models as judges).

📚

Going further

- ⭐ [Blog on several ways to evaluate MMLU](https://huggingface.co/blog/open-llm-leaderboard-mmlu) , by my team at Hugging Face. I recommend reading it if you want to delve deeper into the differences between multi choice log-likelihood evaluations and generative ones, including what it can mean with respect to score changes (The above illustrations come from the blog and have been made by Thom Wolf)
- ⭐ [A beautiful mathematical formalization of the above inference methods](https://arxiv.org/abs/2405.14782v2), from EleutherAI. Go to the Appendix directly.

## [Evaluating with existing benchmarks](https://openevals-evaluation-guidebook.hf.space/#evaluating-with-existing-benchmarks)

Now that you’ve gotten (re)acquainted with required basics on how tokenization and inference work, and what are the caveats when doing evalution, let’s look at actual benchmarking! We’ll first do a small tour of 2025 evaluations, then discuss what to look at in a benchamrk, and why you probably can’t reproduce announcements scores. Lastly, we’ll cover the special case of selecting good benchmark to evaluate training with the FineWeb team.

⚠️

Important concepts

In this section, you’ll see two concepts mentionned quite a lot: contamination and saturation.

**Saturation** is when model performance on a benchmark passes human performance. More generally, the term is used for datasets that are no longer considered useful, as they have lost discriminative power between models.

It’s what you observe in the banner picture!

_If all models have close to the highest possible score on your evaluation, it’s no longer a discriminative benchmark. It’s similar to evaluating high school students on pre-school problems: success tells you nothing (though failure is indicative)._

**Contamination** is when an evaluation dataset ended up in the training dataset of models, in which case the performance of models is artificially inflated, and does not reflect real world performance on the task.

_It’s a bit like evaluating a student on questions it already knows in advance._

### [Benchmarks to know in 2025](https://openevals-evaluation-guidebook.hf.space/#benchmarks-to-know-in-2025)

You can evaluate **specific capabilities** on their own - it’s usually quite interesting to get signal when training, or when comparing base/pretrained models. (However, if you select and validate your training methods with the following evaluations, reporting on them on the final model is slightly biased as you have already oriented your training method towards good results on them).

Feel free to skim this section if you’re not very familiar with evaluation yet, and come back to it once you need to find a dataset for a specific capability :)

#### [Reasoning and commonsense](https://openevals-evaluation-guidebook.hf.space/#reasoning-and-commonsense)

Reasoning and commonsense datasets are often “historic” datasets, built in the age of BERT and embeddings model, before the LLM craze. They were quite challenging at the time (especially because they were often adversarially built for models of the time), but now they are 1) too easy 2) contaminated/saturated, and should only be used for ablations or as pretraining evaluations. The bigger datasets also sometimes contain errors or low quality questions as they tend to have been built through Amazon Mechanical Turk in order to scale up fast and at low cost (what is now done by using LLMs to generate evaluation questions).

[ARC](https://arxiv.org/abs/1803.05457) (2018) (not to confuse with ARC-AGI) is a grade school science MCQA dataset built from human tests. The choices were selected adversarially for word co-occurence systems at the time. It has several subsets, the higher quality `challenge` one is still in use today for pretraining. [WinoGrande](https://openevals-evaluation-guidebook.hf.space/%5Bhttps://arxiv.org/pdf/1907.10641%5D\(https://arxiv.org/pdf/1907.10641\)) (2019) is a crowdsourced (mechanical turk + validation) pronoun resolution/fill in the blank dataset, using adversarial pairs of items to trick models. Both these datasets have been quite hard for models until 2022 to 2023.

A number of historic datasets are looking specifically at reasoning requiring some sort of commonsense understanding and grounding. [HellaSwag](https://openevals-evaluation-guidebook.hf.space/%5Bhttps://arxiv.org/abs/1905.07830%5D\(https://arxiv.org/abs/1905.07830\)) (2019) requires LLMs to select the correct next sentence in a list of adversarial choices, where the text comes from captions in ActivityNet and from tutorials in Wikihow. (It’s the follow up of a dataset called Swag). As most sentences come from tutorials or descriptions of activities, they often require physical commonsense grounding to solve. In the same vein, [CommonsenseQA](https://openevals-evaluation-guidebook.hf.space/%5Bhttps://arxiv.org/abs/1811.00937%5D\(https://arxiv.org/abs/1811.00937\)) (2018) is a dataset of commonsense MCQA built from ConceptNet - annotators write questions, then use conceptually close distractors as options. [PIQA](https://openevals-evaluation-guidebook.hf.space/%5Bhttps://arxiv.org/abs/1911.11641%5D\(https://arxiv.org/abs/1911.11641\)) (2019) is specifically looking at physical commonsense questions (created from examples from [Instructables.com](http://Instructables.com), with again adversarial choices from semantic perturbations or rewriting). [OpenBookQA](https://openevals-evaluation-guidebook.hf.space/%5Bhttps://arxiv.org/abs/1809.02789%5D\(https://arxiv.org/abs/1809.02789\)) (2018) provides open book facts to help answer MCQA questions - however, these questions also require latent common sense knowledge.

A more recent cool reasoning dataset is [Zebra Logic](https://arxiv.org/abs/2502.01100), using logic puzzles to test model reasoning capabilities. Their methods allows for infinite generation of puzzles, so little contamination.

#### [Knowledge](https://openevals-evaluation-guidebook.hf.space/#knowledge)

The main evaluation dataset for knowledge has been [MMLU](https://arxiv.org/abs/2009.03300) (2020). It reached saturation/contamination, and after more in depth examination, a number of issues were identified: incomplete questions referring absent documents, incorrect ground truths, ambiguous questions, and blatant americano-centrism in the topics chosen. It was therefore cleaned in [MMLU-Redux](https://arxiv.org/abs/2406.04127) (2024), extended with more complex questions and more answers in [**MMLU-Pro**](https://arxiv.org/abs/2406.01574) (2024, the main replacement used by the community at the moment), and translated/annotated for cultural bias in [Global-MMLU](https://arxiv.org/abs/2412.03304) (2024). These are used mostly for pretraining evaluations and ablations.

For post training, people look at harder high quality knowledge dataset. [**GPQA**](https://arxiv.org/abs/2311.12022) (2023), custom PhD level questions in biology/chemistry/physics, made to be answerable by PhD students in the correct domain and not otherwise. The most used subset is the `diamond` one, but since its publication in 2023 it has also started reaching contamination.

Last but not least, the pompously named but very high quality [**Humanity’s Last Exam**](https://agi.safe.ai/) (2024) contains 2.5K crowdsourced questions by experts in their field, across domains. It is mostly private, and questions require both complex knowledge and reasoning. It has not been broken yet, and it’s imo a cool dataset. The only issue is that since there is no way to get a model scored fast, people now evaluate against it by using an LLM judge to assess their answers, insted of checking against ground truth, so it’s one of these evaluations where you’ll get really uncomparable results in the wild.

However, though testing models for the raw quality of their latent knowledge made a lot of sense a couple years back (and is still interesting while training to test model quality, with evals like MMLU-Pro during pretraining and GPQA/HLE for post training), I think we will slowly phase out of benchmarks such as this in the next years, for 2 reasons.

1. They are becoming more and more indecipherable for humans: questions are becoming so complex that it’s almost impossible for non experts to understand what performance on each question means (and to make sure the datasets themselves do not contain mistakes)
2. Now that our models are connected to tools, such as internet access, latent knowledge evaluations are increasingly becoming web search and retrieval evaluations, so they make less sense as such. In short, we’re moving from closed book to open book evaluations. As a comparison, in the French school system, you get closed books examinations in high school, but as you enter university, it’s often assumed that you will get access to databases, internet, and scoring becomes less about what you learnt by heart, and more about how you reason given free access to information. I believe this is also a change we will see in LLM evaluation with the increase of model capabilities.

#### [Math](https://openevals-evaluation-guidebook.hf.space/#math)

Math evaluation datasets have been used as proxies for reasoning and logic benchmarking, independently of, obviously, also checking if models can solve math problems.

The two reference math evaluation datasets were [GSM8K](https://arxiv.org/abs/2110.14168) (2021), containing grade school math problems and [MATH](https://arxiv.org/abs/2103.03874) (2021), an aggregation of Olympiad problems present on the web, which reached saturation/contamination in the last years. The former was extended by [GSM1K](https://arxiv.org/abs/2405.00332) (2024), a recreation with 1K new problems, to test which models were contaminated on the former, [GSM-Plus](https://arxiv.org/pdf/2402.19255), a rewriting of models with adversarial changes (distractors, numerical variations, and so forth) and [GSM-Symbolic](https://arxiv.org/abs/2410.05229) (2024), less used, but a very interesting re-writing of GSM8K as problem templates, to prevent contamination: problems can be regenerated ad infinitum.

Community has now been focusing on using:

- The follow ups to MATH, either [**MATH-500**](https://huggingface.co/datasets/HuggingFaceH4/MATH-500) (a representative subset of 500 problems sampled to avoid overfitting) and MATH-Hard (only the 500 hardest questions)
- **AIME** ([24](https://huggingface.co/datasets/HuggingFaceH4/aime_2024), [25](https://huggingface.co/datasets/math-ai/aime25)), american olympiad datasets for high schoolers, taken as is at publication. These datasets are interesting because, since they are made of problems renewed every year with equivalent difficulty, they allow testing for contamination by comparing results at publication with results on the previous year’s dataset
- [**Math-Arena**](https://matharena.ai/), an up to date compilation of competitions and olympiads actualised regularly (it contains AIME25, but a lot of other competitions too!)

Most of these datasets are actually no longer “that hard”, since they stop at grade school level (even though GSM-Symbolic allows to generate problems with more recursion levels, making them synthetically harder). On the other side of the spectrum, [FrontierMath](https://arxiv.org/abs/2411.04872) (2024) was an attempt at providing considerably harder math problems, written individually by mathematicians for the occasion. The dataset was theoretically private (but it appeared OpenAI has had access to parts of the dataset - such a shame). [Humanity’s Last Exam](https://agi.safe.ai/) (2025) (introduced in the knowledge section) also contains interesting “made for the occasion” math problems requiring complex reasoning (notably some theorem proving).

I would personally use AIME25 and MATH-500 for pretraining evaluations, and the Math-Arena for post training.

#### [Code](https://openevals-evaluation-guidebook.hf.space/#code)

Since agents need to interact with tools, they need coding abilities, either to call tools directly if they are code agents, or understand how to debug tool output in case of problems (for code and json agents both, see the difference [here](https://huggingface.co/learn/agents-course/en/unit2/smolagents/tool_calling_agents)). Coding evaluation sets are also good proxies for reasoning.

Historically in 2021, code evaluation sets were [MBPP](https://arxiv.org/abs/2108.07732), 1K crowdsourced Python only entry-level programming problems, [APPS](https://arxiv.org/abs/2105.09938), 10K code generation problems curated from programming interviews and sharing websites, and [HumanEval](https://arxiv.org/abs/2107.03374), introduced with the Codex model, which contrary to the previous is made of “specifically made for the release” problems, which was super neat then! It also came with a sandbox to avoid problematic code execution on the evaluator’s machine. (Last thing this paper introduced was an estimator for `pass@k`, which before that was computed with a literal check on whether an evaluation was a success more than k times on n).

The [EvalPlus](https://openreview.net/pdf?id=1qvx610Cu7) (2023) team made HumanEval+ and MBPP+, extensions of the former, by adding more test cases and fixing bugs in the original datasets as well as adding more inputs. [EvoEval](https://arxiv.org/abs/2403.19114) (2024) also introduced a variation on HumanEval by semantically rewriting the problems and adding difficulty labeling.

For final models, you might want harder or uncontaminated problems.

[**LiveCodeBench**](https://arxiv.org/abs/2403.07974) (2024) follows a similar “grabbing from leetcode websites” approach, but is very interesting because it stores the problem date, to compare model performance on problems created before and after they finished training. This was an excellent contamination free benchmark, and I’m looking forward to an update!

[**AiderBench**](https://aider.chat/docs/leaderboards/) (online since end of 2024 I think?) also uses data from existing coding websites (Exercism to be specific), but goes beyond problem solving by testing specifically code editing and refactoring.

For post training, you want more holistic evaluations, and a couple benchmarks moved beyond evaluation on standalone problems, which were not evaluating complex coding abilities. [RepoBench](https://arxiv.org/abs/2306.03091) (2023) tests repository level auto completion systems in Python or Java, using code from Github as source. It was built by masking random lines in code bases and asking for completions, either a cross file or in file function, and defines several tests level (retrieval, completion, a combination).

[**SweBench**](https://openreview.net/pdf?id=VTF8yNQM66) (2024) is a more well known and complete version of this, also using github, but this time testing if models can solve existing issues, so logic understanding, cross file editing and execution, long context reasoning, etc.

[**CodeClash**](https://codeclash.ai/) (2025) is the coding version of an arena, where models write code which competes against other models code, edit, and iterate.

At this time, I would recommend following LiveCodeBench, AiderBench and the higher quality subset of SWE-Bench (SWE-Bench verified), and reading the [METR report](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) on actual code assistant usefulness.

#### [Long context](https://openevals-evaluation-guidebook.hf.space/#long-context)

To correctly interact with users over a long discussion, without losing track, you need good long context management. (Funny to think that 3 years ago, maximum context lengths for models were 2048 tokens, when now we’re largely at 128K and beyond).

The evaluation which started testing this in 2023 is probably [NIAH](https://github.com/gkamradt/LLMTest_NeedleInAHaystack), (Needle in a Haystack), where you place a random fact in a long unrelated text and ask the model to retrieve it. It provides a neat framework to evaluate where in the context a model is most likely to forget stuff, and from which context length. In 2023 models were really bad at it, in 2025 it’s close to solved.

More complex long context extensions have emerged since. [RULER](https://arxiv.org/pdf/2404.06654) (2024) adds multi-hop tracing (requiring the model to follow chains of variables to get the correct value), word frequency changes, and adds a QA variation of NIAH. it’s also close to solved now. [Michelangelo](https://arxiv.org/pdf/2409.12640v2) (2024, also sometimes called MRCR for multi round co reference) is also using synthetic long context data: tasks (of varying length) test whether models can reproduce precisely unique portions of the context (as well as identify if relevant information is present) and understand sequence of modifications to a text. It was then extended in the [OpenAI MRCR](https://huggingface.co/datasets/openai/mrcr) (2025). [InfinityBench](https://arxiv.org/abs/2402.13718) (2024) is multilingual (En and Zh), and provides 100K tokens synthetic data tasks, across a variety of objectives (QA, retrieval as in NIAH, computations over very long context, …). InfinityBench still provides some signal.

[**HELMET**](https://arxiv.org/abs/2410.02694) (2024) combines tasks and existing benchmarks to get a big single dataset with more signal: RAG and QA datasets (Natural questions, TriviaQA, PopQA, HotpotQA, Narrative QA and InfinityBench), recall (RULER and JSONKV), generation with citation (subsets of ALCE), summarisation, reranking passages (MS MARCO), in context learning (TREC, NLU, Banking77, CLINIC150). Benchmark aggregations are exhaustive but present the risk of measuring things two times : don’t go testing your model against both HELMET and InfinityBench, then aggregating the results, for example, as you would run the same evaluation twice! In 2025, it still has enough discriminative power to compare models.

My favorite long context evaluations ideas are the [Novel Challenge](https://arxiv.org/abs/2406.16264) (2024), 1K true/false claims about fictional books published in the last year (by readers of said books!) requiring having read and understood the full text to answer properly, and the [**Kalamang translation dataset**](https://arxiv.org/abs/2309.16575) (2024), where models need to properly translate from English to Kalamang from reading a grammar book (Kalamang is such a low resource language that it has no online presence - only 200 speakers). The Kalamang translation set could notably be expanded to other low resource languages (but it would be cool to expand to use a rule based grammar checker to test generation validity to get strict accuracy instead of relying on BLEU…).

#### [Instruction Following](https://openevals-evaluation-guidebook.hf.space/#instruction-following)

The two main instruction following datasets are [**IFEval**](https://arxiv.org/abs/2311.07911) (2023) and its extension [**IFBench**](https://arxiv.org/abs/2507.02833) (2025). IFEval is one of the smartest evaluation ideas in the last years, in my opinion: models are asked to follow formatting instructions (about keywords, punctuation, number of words/sentences, file type formatting such as markdown or html, etc). Each of these conditions can be checked with a specific parsing test: this means that this evaluation is one of the rare free form generative evaluation where you can get a strict score without relying on a model judge.

More generally, it falls into the functional correctness/unit test evaluation type, which is my personal favorite way to evaluate models. It’s also very easy to regenerate or extend to prevent contamination.

Side note, but some benchmarks also test “non instruction following” (non compliance): [CoCoNot](https://www.arxiv.org/pdf/2407.12043) (2024) notably tests if models will or won’t comply with incomplete (underspecified/unclear), unanswerable (by lack of information or AI-humanizing, often hallucinations triggering), or unsafe requests. It used manual queries writing, models to write non compliants requests, then filtered to create an eval set presented as a classification problem.

#### [Tool-calling](https://openevals-evaluation-guidebook.hf.space/#tool-calling)

The emergence of tools is one of the features which started moving LLMs into the agentic realm.

[**TauBench**](https://arxiv.org/pdf/2406.12045) (2024) evaluates a model on its ability to answer a user’s query in the retail and airline domains (order/book/look for products/etc). The database mimics real domain data with synthetic samples, and the model is considered correct when 1) its actions updated the database correctly and 2) it answered the user appropriately. To make this benchmark automatic, the user is mocked up by an LLM, which makes this evaluation quite costly to run and prone to errors. Despite these limitations, it’s quite used, notably because it reflects real use cases well.

[ToolBench](https://arxiv.org/pdf/2305.16504) (2023) require calling APIs (OpenWeather, Cat, HomeSearch, TripBooking, GoogleSheets, WebShop, Tabletop, etc) to solve 100 test cases across dataset, requiring between one and 10 tool calls to solve. Some of these APIs are mock ups and some of them are real, which makes the dataset susceptible to accidental failure. It was therefore fixed and extended in [StableToolBench](https://arxiv.org/pdf/2403.07714) (2025), which introduces a general VirtualAPIServer mocking up everything to ensure evaluation stability, however relying on an LLM judge for evaluation, introducing another layer of bias.

[**BFCL**](https://openreview.net/pdf?id=2GmDdhBdDk) (2025, but the benchmark actually has a couple years) evolved considerably over the year, and in its current version contains 4 subset: single turn (simple tool calls), crowdsourced real life function calls from users, multiturn conversations (to test accuracy in long context and query answering with tool calls) and agentic (web search, memory, sql data interaction). It’s using a combination of Abstract Syntax Trees, execution response and state matching (is the final state the expected one) to evaluate if calls are correct. People are focusing on the v3 to test tool calling specifically, and the v4 tests web and search tool use.

Lastly, with the creation of MCPs, some benchmarks arose to test MCP oriented tool calling - however all mostly relying on model judges, and using real world APIs, which can introduce potential failure cases/lack of reproducibility due to network issues (seems like added load for website creators is not too much of an issue as the userbase of most MCP covered is big enough).

[MCPBench](https://arxiv.org/abs/2508.20453) (2025) connects LLMs to live, real world MCP servers (Wikipedia, HF, Reddit, Steam, arxiv, …) with tasks requiring multiple turns to solve (created synthetically). The evaluation combines rule based checks on tool call validity and success with an LLM judge to assess if queries were properly answered.

[**MCP-Universe**](https://arxiv.org/abs/2508.14704) (2025) uses 11 MCP servers across varied real world topics (IRL navigation, 3D design, web search, etc). What’s cool in this one is that evaluation relies on several strict evaluators, one for format correctness, and two for answer correctness: as tasks can be static (asking things that do not change) or dynamic (github stars in a repo, weather, …), in the latter case answer correctness uses a task-dependant execution based evaluation framework which grabs the latest correct answer from the relevant source automatically and compares the model output to it. This is way neater than relying on LLM judge!

[**LiveMCPBench**](https://arxiv.org/abs/2508.01780) (2025) provides a large locally deployable collection of MCP servers to test how good models are at discriminating between tools to accomplish tasks. Best models are already reaching 80% - so we’re close to saturation. However, testing if models can select proper tools in very long lists is a good use case which will be increasingly important as the web goes mcp.

(By the way, here’s a cool [doc](https://www.anthropic.com/engineering/writing-tools-for-agents) on how to write good tools.)

While testing individual capabilities provides valuable signal, real-world assistant performance comes from how these capabilities combine. A model might excel at reasoning but fail when that reasoning must be integrated with tool calling and long context management simultaneously, so we need evaluations requiring the orchestration of multiple capabilities together.

#### [Assistant tasks](https://openevals-evaluation-guidebook.hf.space/#assistant-tasks)

I believe that **assistant tasks** are going to be one of the main ways to do next level evaluations: solving them requires a combination of many capabilities (long context, reasoning, tool calling, …), while the benchmarks themselves provide insight on specific domains performance in a useful real world setup. They also tend to be more understandable (by the general public) than specific capabilities benchmarks. If the benchmarks are general enough, they do not check which precise tools were used, but instead if the end result is correct, as complex tasks allow several paths to success.

**Real life information retrieval**

[**GAIA**](https://arxiv.org/abs/2311.12983) (2023) kickstarted modern agentic evaluation by requiring models to use a combination of tools, reasoning and retrieval to solve real life queries (sometimes including documents). Questions were split in 3 levels, the first one now saturated and the third one still hard for models. It’s also one of these benchs were numbers you find will be spread out against evaluation methods, because people are either reporting on the public validation set or using llm judges to evaluate against the private test set (when there is a public leaderboard [here](https://huggingface.co/spaces/gaia-benchmark/leaderboard)).

It was later replicated in [BrowseComp](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf) (2025) which tests the same thing (can a model find the adequate answer to a specific query using tools and online information) but does not guarantee uniqueness of result, as questions were constructed by starting from the result and building a question from it, with varying levels of difficulty: for example, from a specific paper to retrieve, a question will be created by combining information about metadata, for example “which paper about Topic was published at Conference with one Nationality author and two people from Entity?” However, the benchmark is probably also harder at the moment.

[**GDPval**](https://arxiv.org/abs/2510.04374) (2025) evaluates models on 44 occupations from the “top industries contributing to US GDP”, comparing model performance with human performance using model judges.

Lastly, [GAIA2](https://huggingface.co/blog/gaia2) went beyond simple information retrieval, using a mock up mobile environment to test how assistants are able to answer correctly answer queries relying on chains of events and tool calls. As of now, time sensitive and deliberately noisy subsets (mocking up failing API calls) are the hardest for models, when search and execution seem extremely easy for SOTA models.

**Science assistants**

[SciCode](https://arxiv.org/abs/2407.13168) (2024) tests if models can solve real life scientific problems by writing appropriate scientific code, across stem fields (from biology to math/chem/…). Problems are drawn from real life workflows, and each core issue is decomposed in easier subproblems. For the first version, evaluation was done by scientists and a model judge - models were quite bad at it at publication (less than 5% scores) but I’m unsure where up to date results can be found.

[PaperBench](https://arxiv.org/abs/2504.01848) (2025) similarly tests if models can replicate ML research, but this time with a harder setup: given ICML high quality papers, models must reconstruct the matching code base (8K individually graded tasks have been contributed by the authors of said papers, grouped as rubric trees with weighting for the final grades). Benchmark is evaluated with an LLM judge (though I suspect some of it could be done automatically by constraining a bit the shape of the code asked for).

[DSBench](https://arxiv.org/pdf/2409.07703) (2025) is a multimodal data analysis benchmark using Kaggle and ModelOff (financial data) samples. From the examples in Appendix it seems that questions from ModelOff are provided in a multiple choice setup, which likely makes the task easier, where the Kaggle tasks each have their own metric.

[**DABStep**](https://arxiv.org/abs/2506.23719) (2025) evaluates model on previously private (therefore uncontaminated) operational data analysis workloads using real life questions and data. All problems require multi step reasoning and varied document parsing, as well of course as specific data manipulation skills. It’s a neat eval because it’s hard and replicates actually useful real world use cases, and because each problem has a ground truth, so evaluation is unbiased and not too costly.

Assistant tasks test integrated capabilities in realistic scenarios, but they’re either dynamic and read only, or static in environment which doesn’t change. To evaluate adaptability and dynamic decision-making, we need environments that can “surprise” the model.

#### [Game based evaluations](https://openevals-evaluation-guidebook.hf.space/#game-based-evaluations)

**Game-based** benchmarks are very interesting for several reasons: they usually evaluate adaptability to a changing environment (contrary to most assistant tasks which are static), require long context reasoning, and last but not least, are **understandable** by most people. However, they are not grounded in real life nor necessary reflecting good performance on actually useful use cases.

The most famous formal evaluation among these is probably [ARC-AGI](https://arcprize.org/arc-agi). The first version (2019) was made of puzzles grids in a sequence, where models had to find the last item of said sequence without explicit rules being provided. This benchmark is to me very reminiscent of logic-oriented IQ tests, and it was almost solved in 2024. A similar benchmark (extrapolation of rules) is [Baba is AI](https://arxiv.org/abs/2407.13729) (2024). The latest version of the bench, ARC-AGI3 (2025, ongoing), is still in development, and contains entire new games (requiring exploration, complex planning, memory management, …) made specifically for the benchmark. It is still ongoing, and current best solutions on available problems are bruteforcing the games.

The community and model providers have explored a number of existing games with LLMs. Single player adventure games/RPGs like [TextQuests](https://huggingface.co/blog/textquests) (2025) or [Pokemon](https://github.com/benchflow-ai/benchflow/tree/main/libs/pokemon-gym) (2024) (Twitch for [Claude](https://www.twitch.tv/claudeplayspokemon) and [Gemini](https://www.twitch.tv/gemini_plays_pokemon) for ex) require a combination of very long range planning to get objectives, which require adequante long context memory management, reasoning, and backtracking abilities. Same abilities are needed for single player survival games like [Crafter](https://arxiv.org/abs/2109.06780) (2021, Minecraft inspired). A number of single player game environments have been integrated into the [Balrog](https://arxiv.org/pdf/2411.13543) (2024) benchmark.

Competitive bluffing games like [Poker](https://arxiv.org/html/2501.08328v1) (2025), Mafia variations like [Town of Salem](https://github.com/summersonnn/Town-Of-Salem-with-LLMs) (2025) and Werewolf (2025, [here](https://arxiv.org/abs/2407.13943)/[there](https://werewolf.foaster.ai/)), or [Among us](https://openevals-evaluation-guidebook.hf.space/antimlabs.com/amongais) are very interesting to test logic, reasoning, as well as deception abilities. Claude Opus 4 is for example incapable of winning Town of Salem as a vampire (deceptive role) but does well as a peasant (non deceptive role). Cooperative games like [Hanabi](https://arxiv.org/abs/2510.04980) can also be used to test adaptability and communication ability in a constrained environment.

What’s also very neat about these is that they have a single and unambiguous pass/fail metric: did the LLM win the game or not? At the moment, if I were to use these to evaluate models I would probably look at TextQuests for abilities and Town of Salem for safety.

Beyond testing capabilities in controlled environments, people have explored the ultimate ungameable task: predicting the future.

#### [Forecasters](https://openevals-evaluation-guidebook.hf.space/#forecasters)

In the last year, a new category of impossible to contaminate tasks emerged: forecasting. (I guess technically forecasting on the stock markets can be cheated on by some manipulation but hopefully we’re not there yet in terms of financial incentives to mess up evals). They should require a combination of reasoning across sources to try to solve questions about not yet occuring events, but it’s uncertain that these benchmarks are discriminative enough to have strong value, and they likely reinforce the “slot machine success” vibe of LLMs. (Is the performance on some events close to random because they are impossible to predict or because models are bad at it? In the other direction, if models are able to predict the event correctly, is the question too easy or too formulaic?)

[FutureBench](https://huggingface.co/blog/futurebench) tests if models can predict future news-worthy events. It uses 2 sources: browsing and an LLM generating questions with a weekly time horizon, and user predictions from betting markets. All data is heavily filtered and cleaned before use. For now, models are barely better than random on human created bets, and succeed 3/4th of the time on model generated questions (likely easier).

[FutureX](https://arxiv.org/abs/2508.11987) is similar, but uses an array of specific websites (prediction parkets, government websites, general ranking websites and real time data platforms), then uses templates to generate questions about potential future events (`when will STOCK reach POINT?`). 500 questions are generated daily, with filtering of accidentally irrelevant questions.

A similar approach is used to generate questions in [Arbitrage](https://arxiv.org/pdf/2412.18544), the core difference being the time horizon: events there should be resolved in 2028.

In a similar vein, you’ll also find arenas where LLMs are provided with money to actively trade on financial markets (like Alpha Arena or Trading Agents) - these experiments are less likely to give meaningful results, as, because of their costs, they tend to be run once per model only, so you get no statistical significance there.

#### [Recommendations](https://openevals-evaluation-guidebook.hf.space/#recommendations)

🎯

TLDR

The landscape of evaluation has evolved with the jumps in capabilities, from testing isolated skills to measuring integrated performance in more realistic scenarios.

As of Nov 2025, I recommend using:

- **Core capabilities** (for model builders): Old capabilities evals for training, and for post training AIME26 when it will come out, GPQA, IFEval, SWE-Bench, a long range eval of your choice like HELMET, TauBench or BFCL if you’re targetting tool use
- **Core capabilities** (for comparing models at inference): IFBench, HLE, MathArena, AiderBench and LiveCodeBench, MCP-Universe
- **Long horizon tasks** (for real-world performance): GAIA2, DABStep, SciCode, or domain specific evaluations for your use cases
- **Games** (for some extra fun in measuring robustness and adaptability): ARC-AGI3 when it’s out, TextQuests, Town of Salem if you’re interested in safety, or any other game you like which goes beyond Poker/Chess/Go.

The field is moving toward evaluations that test capability orchestration rather than isolated skills for actual use. This matches our goal of building models that “work well”—systems that can reliably combine core capabilities, tool use, with a good orchestration to solve actual problems.

I hope the field moves towards putting more emphasis on functional testing rather than model judges, and generally understandable datasets and tasks.

If you want to explore even more datasets, you’ll find a big list of older interesting benchmarks [here](https://github.com/huggingface/evaluation-guidebook/blob/main/contents/automated-benchmarks/some-evaluation-datasets.md) with my notes.

### [Understanding what’s in there](https://openevals-evaluation-guidebook.hf.space/#understanding-whats-in-there)

No matter how you selected your initial datasets, the most important step is, and always will be, to look at the data, both what you have, what the model generates, and its scores. In the end, that’s the only way you’ll see if your evaluations are actually relevant for your specific use case.

You want to study the following.

#### [Data creation process](https://openevals-evaluation-guidebook.hf.space/#data-creation-process)

- **Who created the actual samples?** Ideally, you want dataset created by experts, then next tier is paid annotators, then crowdsourced, then synthetic, then MTurked. You also want to look for a data card, where you’ll find annotator demographics - this can be important to understand the dataset language diversity, or potential cultural bias.
    
- **Were they all examined by other annotators or by the authors?** You want to know if the inter-annotator score on samples is high (= are annotators in agreement?) and/or if the full dataset has been examined by the authors. This is especially important for datasets with the help of underpaid annotators who usually are not native speakers of your target language (think AWS Mechanical Turk), as you might otherwise find typos/grammatical errors/nonsensical answers.
    
- **Were the annotators provided with clear data creation guidelines?** In other words, is your dataset consistent?
    

#### [Samples inspection](https://openevals-evaluation-guidebook.hf.space/#samples-inspection)

Take 50 random samples and manually inspect them; and I mean do it yourself, not “prompt an LLM to find unusual stuff in the data for you”.

First, you want to check the content quality.

- Are the prompts clear and unambiguous?
- Are the answers correct? (_Eg: TriviaQA contains several gold answers (aliases field) per question, sometimes conflicting._)
- Is information missing? (_Eg: MMLU references absent schematics in a number of questions._)

It’s important to keep in mind that it’s not because a dataset is a standard that it’s a good one - and this happens because most people skip this step.

Then, you want to check for relevance to your task. Are these questions the kind of questions you want to evaluate an LLM on? Are these examples relevant to your use case?

You might also want to check the samples consistency (especially if you’re planning on using few shots or computing aggregated statistics): do all samples have the same number of choices if it’s a multiple choice evaluation? Is the spacing consistent before and after the prompt? If your evaluation comes with an additional environment, ideally you want to use it to understand what gets called.

Lastly, you also want to quickly check how many samples are present there (to make sure results are statistically significant - 100 samples is usually a minimum for automatic benchmarks).

In the below viewer, for example, you can inspect the first samples of well known post-training benchmarks, collected by Lewis.

#### [Task and metrics](https://openevals-evaluation-guidebook.hf.space/#task-and-metrics)

You want to check what metrics are used: are they automatic, functional, or using a model judge? The answer will change the cost of running evaluations for you, as well as the reproducibility and bias type. Best (but rarest) metrics are functional or based on rule based verifiers

When doing code evals, beware of too easy pass/fail unit tests! Recent LLMs have become very good at overwriting globals to ‘cheat’, especially in languages like Python where you can mess up variable scope.

### [So, you can’t reproduce reported model scores?](https://openevals-evaluation-guidebook.hf.space/#so-you-cant-reproduce-reported-model-scores)

Let’s say you have read a recent tech report about a cool new model, and you want to reproduce their results on your machine… but you’re not managing to? Let’s explore why.

#### [Different code base](https://openevals-evaluation-guidebook.hf.space/#different-code-base)

To reproduce evaluation scores to the decimal point, you first need to make sure you’re using exactly the same code base as the paper you want to reproduce.

Usually, this means either using the evaluation default code as provided by the authors, or a standard implementation in a reference library like Eleuther’s AI `lm_eval` or HuggingFace’s `lighteval`. However, if the code source for evaluation is not provided, then, I’m sorry for you but it’s unlikely that you’ll be able to reproduce the results precisely.

If you want to easily understand what kind of discrepancies happen when using different implementations, you can explore [this blog](https://huggingface.co/blog/open-llm-leaderboard-mmlu) (⭐) we wrote with the eval team at HuggingFace. It studies the differences we observed between 3 common implementations of the MMLU evaluation (in `lm_eval`, `helm`, and in the original author implementation), and how they change model scores.

#### [Subtle implementation or loading difference](https://openevals-evaluation-guidebook.hf.space/#subtle-implementation-or-loading-difference)

We’ve observed that the following were easy things to mess up, even when using the same code base:

- **Different random seeds.**
    - Normally, inference is less affected by random seeds than training. However, they can still affect some CUDA operations (see the PyTorch page on [reproducibility](https://pytorch.org/docs/stable/notes/randomness.html)) and change predictions if you’re using a non greedy generation strategy. They can also affect the prompt if you’re using few-shots, and some pre or post-processing functions. -> A tiny change can result in a couple of points of difference.
- **Actually different metrics**. Metrics can be different in practice even if they share the same name. Some examples:
    - If the original implementation is a _log likelihood_ `exact match` (computing the log probabilities of different possible answers), and you’re using a _generative_ `exact match` (only comparing the main greedy generation with the reference), you won’t get the same scores.
    - We also saw, in evaluation code bases, a number of tasks which were defined as `exact match`, but were actually `prefix exact match` (comparing only the beginning of the generation with the reference), or `suffix exact match` (the opposite), or `quasi exact match` (exact match with a normalization). -> You therefore can’t rely only on the metric name to determine what is happening, and need to look at the code.
- **Different normalization**.
    - To go back to our above `exact match` comparison example, in `lm_eval` v1, a number of tasks were simply named generative `exact match`: you would assume from this that the prediction is _compared as such_ to a reference. Looking at the code, the prediction would instead go through a normalization step (removing punctuation, homogenizing numbers, etc) before being compared to the reference. This will obviously change results quite a lot. (The `lm_eval` v2 now includes the normalization name in most metric names.) -> This is one of the easiest things to mess up, especially for tasks which require a lot of normalization/answer post processing, like math evaluations (where you want to extract the answer from a generated explanation).

🔧

Model loading affects reproducibility

**Four factors that change results even with identical code:**

- **Hardware**: PyTorch doesn’t guarantee reproducibility across different GPUs/hardware
- **Inference library**: transformers, vllm and sglang handle batching and matrix operations slightly differently as of 2025
- **Batch size**: Different batch sizes = different results (you should fix the batch size for reproducibility, though careful about OOM errors)
- **Loading precision**: Lower precision (especially quantized models vs floating point models) will change numerical results

#### [Different prompt](https://openevals-evaluation-guidebook.hf.space/#different-prompt)

3 main things can come into play for prompt variation.

**Prompt itself**

The format you are using for the prompt can and will change scores wildly.

For example, for multichoice question answers, common formats include very simple variations (e.g. using `A` vs `A.` vs `A)` to introduce choices), which, while **semantically equivalent** (as they contain the exact same content) can still result in difference of _several points for the same model_.

📝

Prompt format sensitivity

We did some experiments on this (you’ll see up to a 7 points difference for the same model on the semantically equivalent prompts, the 5 rightmost columns), and a A [paper observed similar results](https://arxiv.org/abs/2310.11324).

**Other example**: Llama 3.1 models predicted correct MATH-Hard answers but scored poorly on the Open LLM Leaderboard, because they overfit to GSM8K’s prompt format and couldn’t adapt to the new one for this eval, despite it being provided in few shot examples.

_Evaluation on MMLU subsets, acc_norm score (seed 0), in 5-shot._

49.050.552.154.556.455.455.557.037.641.843.547.950.851.222.947.744.648.047.653.554.254.956.450.739.144.346.546.147.148.451.745.843.648.949.551.051.352.052.852.3ABCDEFGHMistral-7B-v0.1Qwen1.5-7Bgemma-7bphi-2DeciLM-7B

Prompt Formats:

A....? -> choice1/choice2/...

B.Q:...? A: -> choice1/choice2/...

C.Question: ...? Answer: -> choice1/choice2/...

D.Question: ...? Choices: ... Answer: -> choice1/choice2/...

E.Question: ...? Choices: A. ... Answer: -> choice1/choice2/...

F.Question: ...? Choices: (A) ... Answer: -> choice1/choice2/...

G.Question: ...? Choices: A. ... Answer: -> A/B/C/D

H.Question: ...? Choices: (A) Answer: -> (A)/(B)/(C)/(D)

This [great paper](https://arxiv.org/abs/2407.07890)⭐ also highlights a side effect of this: a number of models are now trained to overfit benchmark prompts and answer formats, to the cost of adaptation to other prompts at evaluation time.

Some tasks are also prefixed with a task prompt (eg: `The following questions are about <topic>`) - its presence or absence will also affect the scores.

**System prompt and chat template**

Chat models usually have been through instruction/preference training or fine-tuning. During this stage, they have learned to follow specific templates when inferring. For example, templates can require starting rounds of dialogue with a general prompt (called the `system prompt`) prefixed by specific tokens (usually `System:` ). Said prompt is here to provide high-level instructions for the model, such as the contents of a persona, or general answering style instructions. Rounds of dialogue can also require adding prefix key words to text, such as `User` for queries and `Assistant` for answers.

When using few shot, you also need to select if you want examples to be provided multi-turn (mimicking user/assistant turns) or all at once (in a single user prompt).

Not following the chat template expected by the model at inference will kill its performance, as it will drive its output outside of the probability space it’s been converging on.

Similarly, if you are using a reasoning model, you need to make sure whether you are comparing with or without thinking enabled.

**Few-shots samples**

Two things are easy to mess up with few-shot samples: the number of few-shot examples, which ones you are using, and their specific ordering

The importance of using the same examples is not too surprising, if we assume some samples are better at expressing the task than others. More surprising maybe: you not only need to use the exact same samples, but also present them in the **exact same order**. Varying the order on the same samples led us to observe up to 3 points of difference on some subsets of MMLU (you can see [some results here](https://huggingface.co/blog/evaluation-structured-outputs) , it’s the third colorgrid)

This is also a place where paying attention to the random seeds is important.

**Parameters**

For generative evaluations, parameters to pay attention to are making sure you are 1) using the **same end of sentence token** (you probably should not be using a default one for chat and reasoning models); 2) allowing your model to **generate the same number of tokens** for the evaluation (this is particularly crucial for reasoning models, which require a huge numbers of tokens in thinking mode); 3) if using sampling, that you are using the **same seed/temperature parameters**.

### [Selecting good benchmarks automatically for model training](https://openevals-evaluation-guidebook.hf.space/#selecting-good-benchmarks-automatically-for-model-training)

In some cases, you don’t want to “just” reproduce existing scores a posteriori, but you actually need to understand how well your model is training while it’s happening. Evaluations you need then have different properties than evaluations for the final performance of models, as you need tasks which will provide good signal even when the model is not yet very good.

So the FineWeb team designed a method to select the best evaluations for pre-training ablations, across 9 languages - let’s listen to their wise advice.

For these languages, we collected and implemented all available tasks that we could find, a total of **185 tasks**. Then, we began task selection with two primary goals: ensuring **evaluation diversity**, and making sure each task provided a **reliable signal** during pre-training.

For evaluation diversity, we aimed to assess a broad range of model capabilities, including:

- **Reading comprehension (RC)**: Understanding provided context and answering questions based on it.
- **General knowledge (GK)**: Answering questions about facts from various fields without added context.
- **Natural Language Understanding (NLU)**: Comprehending the semantics of provided input.
- **Common-sense reasoning (RES)**: Demonstrating the ability to perform simple reasoning requiring embodied knowledge.
- **Generative tasks**: Ability to generate text in the target language without the “help” of multiple choice options.

We consider that tasks provide a reliable signal if they provide a dependable score. This means the score should be above the random baseline, increase as training progresses, show low variability across different seeds, and provide consistent model ranking at each training stepFor similar sized models trained with the same hyperparameters on the same amount of data..

To thoroughly examine the signal our tasks provide, we trained many 1.5B parameter models for each language, using 30B tokens from subsets of the supported languages of the five largest openly available multilingual web datasets. These models were trained with the same hyperparameters and tokenizer. We then evaluated them at regular checkpoint intervals on the collected tasks (with no instruction and no system prompt in a 0-shot setting).

This process required multiple evaluation runs for each task due to iterations on its implementation, resulting in a total of **73 000 GPU hours consumed** 🔥!

With **49 models trained** we could finally define what a **reliable signal** means to us!

#### [Monotonicity](https://openevals-evaluation-guidebook.hf.space/#monotonicity)

One of our core requirements for a task is that it can be learned from training data and this **learning can be gradually observed as the training progresses**. Without this improvement through time, it’s uncertain whether there will ever be an improvement in the future.

To measure this, we used the **Spearman rank correlation** to quantify the correlation between steps and score. Spearman rank correlation can capture monotonicity even when scores don’t evolve linearly with the number of steps. We required each task to have at least an average correlation of 0.5 over all model training runs.

✅ Good monotonicity: mlmm_hellaswag_fra_cf [fr]

05.0101520250.30.30.40.4Training Tokens (billions)ScoreBaseline

CommonCrawlDataset-ADataset-BDataset-CDataset-D

Monotonicity: 0.98

❌ Bad monotonicity: mlmm_truthfulqa_ara_cf:mc1 [ar]

05.0101520250.20.20.30.30.30.3Training Tokens (billions)ScoreBaseline

CommonCrawlDataset-ADataset-BDataset-CDataset-D

Monotonicity: -0.26

#### [Low noise](https://openevals-evaluation-guidebook.hf.space/#low-noise)

When comparing model performance on tasks, we need to consider whether differences are due to **evaluation noise or genuine performance variations**.

Noise can arise from the stochastic processes involved in model training, such as random token sampling, data shuffling, or model initialization ([Madaan et al., 2024](https://arxiv.org/abs/2406.10229)). To measure how sensitive each task is to this noise, we trained four additional models on our own monolingual corpora (unfiltered CommonCrawl data in each language) using different seeds.

For each task, we computed:

1. First, a standard deviation of model scores for every step (approximately every 1B tokens), which we call the **per-step-std**.
2. Then, to obtain a global variability measurement, we averaged all the per-step-std values to get the **avg-std** over the full training. We assume this value is an upper-bound across model architectures and training datasets (as it was approximated by models trained on a “dirtier” dataset, therefore with higher variability).
3. Finally, we computed the **signal-to-noise ratio** (SNR) as the main metric for task variability. We calculate SNR as the mean score at 30B tokens of all runs divided by the avg-std. This metric measures how significant the overall score is relative to the score variations (noise).

We aimed for each task to have an SNR > 20. The only exception to this rule are generative tasks, which typically have relatively low SNR, but are still worth including as they provide insights into how the model behaves when prompted to generate unconstrained (without answer options). In a multilingual setting, this is particularly relevant as some models trained on multiple languages can exhibit high task scores but then suddenly reply in the wrong language for generative tasks!

✅ Good SNR: xstory_cloze_tel_cf [te]

05.0101520250.50.50.50.50.50.60.6Training Tokens (billions)ScoreBaseline

CommonCrawl_5CommonCrawl_6CommonCrawl_7CommonCrawl_8

SNR: 87.87

❌ Bad SNR: tydiqa_tel [te]

05.01015202500.00.00.10.10.1Training Tokens (billions)ScoreBaseline

CommonCrawl_5CommonCrawl_6CommonCrawl_7CommonCrawl_8

SNR: 6.40

Assuming model performance is normally distributed across different seeds, we want the benchmark-run performance to be at least 3 final-stds above the benchmark random baseline. This would mean that 99.85% of seed scores are above the random baseline (formally, benchmark-run performance - benchmark random baseline > 3 * final-std).

#### [Non-Random Performance](https://openevals-evaluation-guidebook.hf.space/#non-random-performance)

Many model capabilities are acquired later in training, thus **many tasks** (especially harder ones, such as math-related ones) **show baseline-level performance for an extended period**. While these tasks are useful, they’re not ideal for early pre-training evaluation, and **we did not want to keep them** for this setting.

We first computed the baseline random performance of the task (as the sum of 1/n_choices for all samples for multiple choice questions, and as zero for generative evaluations). Then we calculated the task’s distance from the baseline as the maximum score across all models minus the baseline.

✅ Non-random: agieval_zho_cf/acc_pmi [zh]

05.0101520250.30.30.30.30.3Training Tokens (billions)ScoreBaseline

CommonCrawlDataset-ADataset-BDataset-CDataset-D

Non-Randomness: 21.44

❌ Random perf: agieval_zho_cf/acc [zh]

05.0101520250.20.20.20.3Training Tokens (billions)ScoreBaseline

CommonCrawlDataset-ADataset-BDataset-CDataset-D

Non-Randomness: -8.84

#### [Model Ordering Consistency](https://openevals-evaluation-guidebook.hf.space/#model-ordering-consistency)

Let’s not forget that the main goal of these evaluations is to compare models and datasets!

In the future, we want to use these evaluations to select the best datasets for full model pretraining. This means **our tasks should rank datasets trained using very few tokens (we typically run data ablations on 30B tokens), in the same order as they would when trained for longer, after significantly more steps.**

In other words, we would like tasks to have **predictive capability regarding future performance during pre-training**: if pre-training dataset A outperforms pre-training dataset B at 30 billion tokens, we would like this trend to continue at 300 billion tokens.

Proving this is inherently impossible, but there is a necessary preliminary condition that we can test for: for the results to be consistent at large scales, they must also first show consistency at smaller scales!

To measure this consistency in task ordering, we computed the average **Kendall’s Tau** of models ranking between every two consecutive steps. We only considered steps starting after 15B tokens of pre-training, as we found orderings before the range incredibly noisy. A high value of this metric indicates that the ordering remains consistent as training progresses.

We had no strict minimum value requirement for this property, instead using it to establish comparisons between tasks.

✅ Good ordering: xcsqa_ara_cf [ar]

05.0101520250.20.20.20.20.30.3Training Tokens (billions)ScoreBaseline

CommonCrawlDataset-ADataset-BDataset-CDataset-D

Kendall's Tau: 0.83

❌ Bad ordering: thai_exams_tha_cf [th]

05.0101520250.20.20.20.3Training Tokens (billions)ScoreBaseline

CommonCrawlDataset-ADataset-BDataset-CDataset-D

Kendall's Tau: 0.69

#### [Metrics](https://openevals-evaluation-guidebook.hf.space/#metrics)

As the targets in CF of multiple choice tasks are choices themselves, each target can have a different number of tokens, characters, and unconditional probability (probability of generating the choice without a context prefix).

Measuring accuracy without normalization would have the models prefer answers with fewer tokens, for example.

To account for this, we consider the following accuracy variations:

- **Accuracy** : `acc` = (ln(P(ai∣q)))iargmax​(ln(P(ai​∣q)))
- **Accuracy normalized over character length** : `acc_char` = ln(P(ai∣q))num_characters(ai)iargmax​num_characters(ai​)ln(P(ai​∣q))​
- **Accuracy normalized over token length** : `acc_token` = ln(P(ai∣q))num_tokens(ai)iargmax​num_tokens(ai​)ln(P(ai​∣q))​
- **PMI Accuracy** : `acc_pmi` = lnP(ai∣q)P(ai∣u)iargmax​lnP(ai​∣u)P(ai​∣q)​, where u=u= ”Answer:”

Where aiai​ is the answer choice ii, qq is a question prompt and P(ai∣q)P(ai​∣q) is the probability of having aiai​ follow qq. For more details see [Gu et al., 2024](https://arxiv.org/abs/2406.08446) and [Biderman et al., 2024](https://arxiv.org/abs/2405.14782).

`acc_pmi` metric measures how much more likely a model is to predict A_i if provided with question context compared to if there was no context at all. This can be useful if the correct choice contains generally unlikely tokens, making the model less likely to choose such an answer.

For our generative tasks on the other hand, we used the following metrics:

- `prefix_match`: Exact match where only the prefix of the answer must match
- `f1`: F1 score computed over predicted/gold words extracted using a word tokenizer

For both generative metrics, minor preprocessing is applied to remove articles and punctuation, and lowercase the text.

Selecting the best evaluation metrics proved to be a **challenging task**. Not only is there no single metric that consistently outperforms the rest, but we often encountered situations where one metric had better monotonicity while another had a higher signal-to-noise ratio. In such cases, we typically made our decision based on the selected metric for tasks’ implementation in a different language. We are aware that such hand-picking is often not possible and thus offer the following recommendations:

➡️ Multichoice Tasks

- We found **base accuracy** to perform well for tasks with answer options varying subtly (e.g. Yes/No/Also), particularly NLI tasks. In such cases, where the answer options are often each a single token, the base accuracy is advisable to use.
- While OLMES authors ([Gu et al., 2024](https://arxiv.org/abs/2406.08446)) recommends using PMI for tasks with unusual words, we found **PMI** to be highly effective for “difficult” reasoning and knowledge tasks like AGIEVAL or MMLU. In these cases, PMI provided the best results and was often the only metric delivering performance above random. That said, PMI was, on average, the weakest metric across all other tasks, while also being two times more expensive to compute. We therefore only recommend its use for complex reasoning and knowledge tasks.
- The metrics we found to be **most reliable overall** were length normalization metrics (token or character-based). However, the best choice was dependent on language, rather than being consistent for a given task. Due to that, we recommend using the maximum of acc_char and acc_token for the most reliable results.Note that acc_token is heavily tokenizer dependent. On our ablations all models were trained using the same tokenizer.

➡️ Generative Tasks

For **generative metrics**, the choice is clearer: we suggest using the F1 score unless exact matching is required, as in math-related tasks. F1 is generally less noisy and more resilient to small changes in the generations.

## [Creating your own evaluation](https://openevals-evaluation-guidebook.hf.space/#creating-your-own-evaluation)

At this stage, you likely have a good idea of why people do evaluation, which benchmarks exist and are relevant for different model stages (training, inference of base and tuned models), but what if nothing exists for your specific use case?

This is precisely when you could want to create your own evaluation.

### [Dataset](https://openevals-evaluation-guidebook.hf.space/#dataset)

#### [Using existing data](https://openevals-evaluation-guidebook.hf.space/#using-existing-data)

You can use existing datasets are are, and change the prompting or metrics associated (as has been done for older evaluations to adapt them to new prompting method), but you can also aggregate datasets.

Dataset aggregation is a good approach when you want to evaluate a specific capability that isn’t well-covered by a single benchmark. Rather than starting from scratch, you can combine samples from multiple existing datasets to create a targeted evaluation suite. That’s for examples what the authors of the “Measuring AGI” paper did recently to try to create a new “AGI evaluation” dataset.

When aggregating datasets, pay attention to whether

- they contain redundant data (most mathematics datasets are rewrites or aggregations of the same initial problems)
- you need balanced representation across sources (you might not want one dataset to dominate and skew your evaluation) - this will also determine whether to aggregate scores across all samples or per subset
- formats and difficulty levels are compatible (typically, if creating a unified dataset, beware of mixing up samples requiring sampling or not).

Examples: MMLU, Big-Bench (hundreds of diverse tasks), and HELM (combines multiple existing benchmarks for holistic evaluation)

New research by EpochAI (2025) showcases how to [best aggregate benchmarks together under a single framework](https://epoch.ai/blog/a-rosetta-stone-for-ai-benchmarks) to make the aggregated dataset harder overall and less prone to saturation.

#### [Using human annotators](https://openevals-evaluation-guidebook.hf.space/#using-human-annotators)

I suggest reading Section 3 of this [review](https://aclanthology.org/2024.cl-3.1/) of good practices in data annotation quality. If you want production level quality and have the means to implement all of these methods, go ahead!

Annotation Process

- Iterative Annotation
- Careful Data Selection
- Annotation Scheme
- Guideline Design
- Pilot Study
- Validation Step

Annotators

- Workforce Selection
- Qualification Test
- Annotator Training
- Annotator Debriefing
- Monetary Incentive

Quality Estimation

- Error Rate
- Control Questions
- Agreement

Quality Improvement

- Correction
- Updated Guidelines
- Filtering
- Annotator Feedback
- Annotator Deboarding

Adjudication

- Manual Curation
- Majority Voting
- Probabilistic Aggregation

**Figure 1:** Data annotation best practices recommended by the comprehensive review at aclanthology.org/2024.cl-3.1 - check out their Section 3.

However, important guidelines (no matter your project size) are the following, once you defined your task and scoring guidelines.

- **Workforce selection, and if you can monetary incentive** You likely want the people working on your task to:

1. obey some demographics. Some examples: be native speakers of the target language, have a higher education level, be experts in a specific domain, be diverse in their geographical origins, etc. Your needs will vary depending on your task.
2. produce high quality work. It’s notably important now to add a way to check if answers are LLM-generated, and you’ll need to filter some annotators out of your pool. _Imo, unless you’re counting on highly motivated crowdsourced annotators, it’s always better to pay your annotators correctly._

Unless you have highly motivated crowdsourced annotators, always pay fairly. Underpaid annotators produce lower quality work, introduce more errors, and may use LLMs to complete tasks quickly.

- **Guideline design** Make sure to spend a lot of time really brainstorming your guidelines! That’s one of the points on which we spent the most time for the [GAIA](https://huggingface.co/gaia-benchmark) dataset.

When creating the [GAIA benchmark](https://huggingface.co/gaia-benchmark), guideline design consumed more time than any other phase. Clear, unambiguous guidelines are worth the investment—they prevent costly re-annotation rounds.

- **Iterative annotation** Be ready to try several rounds of annotations, as your annotators will misunderstand your guidelines (they are more ambiguous than you think)! Generating samples several times will allow your annotators to really converge on what you need.
    
    - **Quality estimation** and **Manual curation** You want to control answers (notably via inter-annotator agreement if you can get it) and do a final selection to keep only the highest quality/most relevant answers.

Specialized tools to build annotated high quality datasets like [Argilla](https://argilla.io/) can also help you.

Going further

- ⭐ [How to set up your own annotator platform in a couple minutes](https://huggingface.co/learn/cookbook/enterprise_cookbook_argilla), by Moritz Laurer. A good read to get some hands on experience using open source tools (like Argilla and Hugging Face), and understanding better the dos and don’ts of human annotation at scale.
- ⭐ [A guide on annotation good practices](https://aclanthology.org/2024.cl-3.1/). It’s a review of all papers about human annotation dating from 2023, and it is very complete. Slightly dense, but very understandable.
- [Another guide on annotation good practices](https://scale.com/guides/data-labeling-annotation-guide), by ScaleAI, specialised in human evaluations. Its a more lightweigth complement to the above document.
- [Assumptions and Challenges of Capturing Human Labels](https://aclanthology.org/2024.naacl-long.126/) is a paper on how to look at source of annotator disagreement and mitigate them in practice

#### [Creating a dataset synthetically](https://openevals-evaluation-guidebook.hf.space/#creating-a-dataset-synthetically)

**Using rule-based techniques**

If your task allows, using procedurally generated benchmarks is a very good way to get a virtually infinite supply of samples and avoid contamination! They can generate unlimited fresh test cases algorithmically, while controlling difficulty and enabling automatic verification, ensuring models haven’t seen examples during training.

For some examples, you can look at [NPHardEval](https://arxiv.org/abs/2312.14890), [DyVal](https://arxiv.org/abs/2309.17167), [MuSR](https://arxiv.org/abs/2310.16049), [BabiQA](https://arxiv.org/abs/1502.05698), [ZebraLogic](https://arxiv.org/pdf/2502.01100), IFEval, or GSMTemplate among others. **NPHardEval** generates complexity-grounded tasks like graph problems with automatic verification and monthly refreshes to reduce overfitting. **MuSR** creates complex reasoning instances like 1000-word murder mysteries using neurosymbolic generation. **ZebraLogic** algorithmically produces logic grid puzzles by generating solutions and iteratively minimizing clues using SAT solvers. **BabiQA** simulates entities following successions of actions. **IFEval** tests instruction-following with 500+ prompts containing verifiable constraints like word counts that can be checked programmatically. **GSM-Symbolic** uses templates to generate diverse math questions.

Tasks which usually fit this paradigm test mathematical, logical, or coding abilities.

**Creating synthetic data with models**

If you want to create synthetic data, you usually start from a number of seed documents that will act as your ground truth. These can be internal and specific to your use cases, or available on the web and of high quality (like Wikipedia, Stack Overflow, …). You’ll then likely need to chunk your data into units of self contained meaning.

You’ll then likely want a model to design questions from your data. For this, you will need to select a frontier model, and design a very good prompt asking the model to create use-case relevant questions from the provided data. It’s better if you ask the model to provide the source on which it based its question.

You can also use seed prompts as examples to provide to an external model for it to write the prompt for your model to generate new questions, if you want to go full synthetic ^^

Once this is done, you can do an automatic validation by using a model from a different family line on your ground truth + questions + answer as a model judge.

⚠️

Always make sure that you're checking your data

No matter how tempting it is to do everything automatically, you should always check your data at every step, to make sure your evaluations are qualitative. Evaluation is the name of the game and you need to use extremely good data.

#### [Managing contamination](https://openevals-evaluation-guidebook.hf.space/#managing-contamination)

In general, you should assume that a dataset publicly available on the internet is or will be contaminated.

Solutions to mitigate this include:

- providing a **canary string** in the evaluation set (like in [BigBench](https://github.com/google/BIG-bench)): it is a specific character combination that model creators can look for in their training sets, which would indicate that it contains an evaluation
- providing evaluation sets in **[encrypted](https://arxiv.org/abs/2309.16575) or [gated](https://huggingface.co/datasets/Idavidrein/gpqa)** forms so that they can’t be parsed easily by web crawlers - therefore not ending up accidentally in training sets
- running [dynamic benchmarks](https://arxiv.org/abs/2104.14337): benchmarks regularly updated through time so that models can’t “learn the answers by heart” (but it makes datasets more costly)
- if you are running a benchmark, trying to [detect contamination](https://arxiv.org/abs/2311.06233) post-hoc (for example, by looking at the generation perplexity or designing adversarial versions of the prompts - however, no method is a foolproof contamination detection method)

However, it’s not because a dataset is contaminated that it won’t still be interesting and have signal during training, as we saw in the ablations section.

A model which can only predict well on its training data (and has not latently learnt more high-level general patterns) is said to be **overfitting**. In less extreme cases, you still want to test if your model is able to generalize to data patterns which were not in the training set’s distribution (for example, classify toxicity on stack overflow after having seen only toxicity on reddit).

### [Choosing a prompt](https://openevals-evaluation-guidebook.hf.space/#choosing-a-prompt)

The prompt is going to define how much information is given to your model about the task, and how this information is presented to the model. It usually contains the following parts: an optional **task prompt** which introduces the task, and the format that the output should follow, **attached context** if needed (for example a source, an image), a **problem prompt** which is what you ask of the model, and optional options for multiple choice evaluations.

When defining your prompt, you need to be aware that even small changes in semantically equivalent prompts can make the results vary by quite a lot, and prompt formats might advantage or disadvantage specific models (See [this section](https://huggingface.co/spaces/OpenEvals/evaluation-guidebook#different-prompt)).

➡️ This can be mitigated by re-running the evaluation several times with prompt variations (but it can be costly), or simply running your evaluation once using a range of prompt formats allocated to different samples of equivalent difficulty.

➡️ You can also provide examples to your model to help it follow the expected format (using few-shot examples), and adding connector words helps this overall.

### [Choosing an inference method for your model](https://openevals-evaluation-guidebook.hf.space/#choosing-an-inference-method-for-your-model)

You’ll need to choose what kind of inference method you need.

Reminder about loglikelihood evaluations

Using log-probabilities is good for multiple choice question answers (MCQA), to test model knowledge, or ability to disambiguate.

- Pros:
    - Makes sure that all models have access to the correct answer
    - Provides a proxy for model “confidence” (and calibration)
    - Fast to evaluate, especially when we ask the model to predict only one token (A/B/C/D the indices of the choices, or Yes/No, etc).
    - Allow to get signal on small models’ task performance
- Cons:
    - Slightly over-scores small models which would have generated something outside of the range of available choices if given free rein.
    - Some models [favor specific choices based on the order in which they have been presented](https://arxiv.org/abs/2309.03882), which could lead to unrepresentative evaluations (unless you’re re-running the evaluation n times by shuffling samples orders, which you should do for significance if you have the budget for!)

💡

Tip: an easy speed up for MCQA evaluations

You can speed up your MCQA predictions by a lot if you make sure your model needs to predict only one token for the task.

This way, instead of running your `number_of_choices` predictions (`context + choice 1`, `context + choice 2`, etc), you can simply run inference on `context` and compute the probability distribution on the full vocabulary (which will include all your one token choices) to get your logprobabilities of interest, and do this step in one pass.

Reminder about generative evaluations

Nowadays most evaluations are generative: using generations is very good for any task where you want to test fluency, reasoning, or the ability of your model to actually answer questions. It’s also the most relevant way to evaluate reasoning models.

- Pros:
    - Should actually correlates with LLM ability to generate fluent text, will most of the time be what people are actually interested in
    - The only way to evaluate both closed and open source models
- Cons:
    - Can be harder to score (see below)
    - More expensive than log likelihood evaluations, especially if they include sampling or reasoning models

### [Scoring](https://openevals-evaluation-guidebook.hf.space/#scoring)

If you are looking at **log-probabilities**, your metrics are going to be easy: you’ll likely want to look at a variant of accuracy (how often the most likely choice is the best choice). It’s important to normalize it by sequence length (either character, token, or pmi). You could also look at perplexity, recall, or f1 score.

If you’re looking at **generative** evaluations, this is where it gets trickyyy, so the next chapter is specifically on this!

## [Evaluation’s main challenge: Scoring free form text](https://openevals-evaluation-guidebook.hf.space/#evaluations-main-challenge-scoring-free-form-text)

Scoring free-form text is tricky because there are typically many different ways to express the same correct answer, making it hard to determine semantic equivalence through simple string matching, and output variations can make two semantically identical answers look completely different. Responses can be partially correct or contain a mix of accurate and inaccurate information. There can even be no single ground truth for the problem at hand, for example for tasks requiring to judge coherence, helpfulness, and style, which are inherently subjective and context-dependent.

### [Automatically](https://openevals-evaluation-guidebook.hf.space/#automatically)

When there is a ground truth, however, you can use automatic metrics, let’s see how.

#### [Metrics](https://openevals-evaluation-guidebook.hf.space/#metrics)

Most ways to automatically compare a string of text to a reference are match based.

This is more interesting to do on data that was not included in the model training set, because you want to test if it **generalizes** well. You don’t want a model which can only predict text it has already “seen”, that would not be very useful!

The easiest but least flexible match based metrics are **exact matches** of token sequences. While simple and unambiguous, they provide no partial credit - a prediction that’s correct except for one word scores the same as one that’s completely wrong.

Be aware that “exact match” is used as a catch all name, and also includes “fuzzy matches” of strings: compared with normalization, on subsets of tokens (prefix only for ex), etc

The translation and summarisation fields have introduced automatic metrics which compare similarity through overlap of n-grams in sequences. **BLEU** (Bilingual Evaluation Understudy) measures n-gram overlap with reference translations and remains widely used despite having a length bias toward shorter translations and correlating poorly with humans at the sentence level (it notably won’t work well for predictions which are semantically equivalent but written in a different fashion than the reference). **ROUGE** does a similar thing but focuses more on recall-oriented n-gram overlap. A simpler version of these is the **TER** (translation error rate), number of edits required to go from a prediction to the correct reference (similar to an edit distance). Lastly, you’ll also find model-based metrics using embedding distances for similarity like **BLEURT** (it uses BERT-based learned representations trained on human judgments from WMT, providing better semantic understanding than n-gram methods, but requiring a model download and task-specific fine-tuning for optimal performance). I’m introducing here the most well known metrics, but all of these metrics have variations and extensions, among which CorpusBLEU, GLEU, MAUVE, METEOR, to cite a few.

REF:My cat loves doing model evaluation and testing benchmarks

PRED:My cat enjoys model evaluation and testing models

Exact Match

0.0

Binary: 1 or 0

✗ Strings differ

Most strict metric - no partial credit

Translation Error Rate

0.333

Edit distance normalized

**3** edits / **9** words = **0.333**

Edit operations:

• Insert "**loves**"

• Replace "**enjoys**" → "**doing**"

• Replace "**models**" → "**benchmarks**"

Lower is better (0 = identical)

BLEURT

0.318

Semantic similarity

BLEURT uses BERT embeddings learned from real text.

BLEU

0.523

N-gram precision-based

**1-gram:** 6/8 (75%)

mycatmodel +3 more

**2-gram:** 4/7 (57%)

my catmodel evaluationevaluation and +1 more

**3-gram:** 2/6 (33%)

model evaluation andevaluation and testing

ROUGE-1

0.706

Unigram-based F1

**Recall:** 67% | **Precision:** 75%

Matched unigrams:

mycatmodelevaluationand +1 more

ROUGE-2

0.533

Bigram-based F1

**Recall:** 50% | **Precision:** 57%

Matched bigrams:

my catmodel evaluationevaluation and +1 more

Once you have an accuracy score per sample, you can **aggregate** it across your whole set in several ways. In general, people average their results, but you can do more complex things depending on your needs. (Some metrics already come with an aggregation, like CorpusBLEU).

If your score is **binary**, look at the **precision** (critical when false positives are costly), **recall** (critical when missing positives is costly), **F1 score** (balances precision and recall, good for imbalanced data), or **MCC** (Matthews Correlation Coefficient, which works well with imbalanced datasets by considering all confusion matrix elements). If your score is **continuous** (less likely though), you can use **mean squared error** (penalizes large errors but heavily weights outliers) or **mean absolute error** (more balanced than MSE).

If you assume your data should follow a specific linear regression model (for example if you are studying model calibration), you can look at measures like the **R²** or correlation coefficients like **Pearson** (for linear relationships, assumes normality) or **Spearman** (for monotonic relationships without normality assumptions). However, it’s a bit out of scope here.

More generally, when picking your metric and its aggregation, you need to keep in mind what your task is really about. For some domains (ex: medical, chatbots with public interaction), you don’t want to measure the average performance, but need a way to evaluate the **worst performance** you’ll get (on medical quality of output, on toxicity, etc).

To go further

- This [blog](https://ehudreiter.com/2024/07/10/challenges-in-evaluating-llms/) covers some of the challenges of evaluating LLMs.
- If you’re looking for metrics, you’ll also find a good list with description, score ranges and use cases in [this organisation](https://huggingface.co/evaluate-metric).

Pros and cons of using automated metrics

Automated benchmarks have the following advantages:

- **Consistency and reproducibility**: You can run the same automated benchmark 10 times on the same model and you’ll get the same results (baring variations in hardware or inherent model randomness). This means that you can easily create fair rankings of models for a given task.
- **Scale at limited cost**: They are one of the cheapest way to evaluate models at the moment.
- **Understandability**: Most automated metrics are very understandable.

However, they also present have a **reduced use on more complex tasks**: an automatic metric either requires you to have a perfect, unique and unambiguous reference/gold, like for tasks where performance is easy to define and assess (for example, classification of toxicity, knowledge questions with a single answer). More complex capabilities, on the other hand, are harder to decompose into a single and simple answer.

#### [Normalization](https://openevals-evaluation-guidebook.hf.space/#normalization)

Normalization means changing a string of characters to have it fit a specific reference format. For example, when comparing a model prediction to a reference, you usually don’t want to penalize extra spacing in the prediction, or added punctuation or capitalisation. That’s why you normalize your prediction.

They are vital for specific tasks, such as math evaluations, where you want to extract an equation from a longer prediction, and compare it to a reference. In the below table, we make a list of some issues we saw happening when extracting predictions from model outputs using SymPy naively for the MATH dataset, and how Math-Verify, a specific math parser, solved these.

|📄 Example|❗️Issue|✅ Math-Verify|🛑 Naive Approach|
|---|---|---|---|
|Therefore, the perimeter of one of these triangles is 14+7214+72​ inches, expressed in simplest radical form.|Failed extraction|`7*sqrt(2) + 14`|None|
|Therefore, the sum of the infinite geometric series is (\frac79).|Failed extraction|`7/9`|None|
|The final answer is 2x+4y+z−19=02x+4y+z−19=0. I hope it is correct.|Partial parse of parametric eq|Eq(2_x + 4_y + z - 19, 0)|0|
|(23)|Failed extraction due to latex borders|`23`|None|
|((- \infty, -14) \cup (-3, \infty)).|Failed extraction due to interval|Union(Interval.open(-oo, -14), Interval.open(-3, oo))|None|
|100%|Failed extraction due to invalid symbol|`1`|None|
|1/3 == 0.333333|No rounding support|True|False|
|sqrt(1/2)*7 == sqrt(0.5)*7|No numerical evaluation support|True|False|

Look at [this blog](https://huggingface.co/blog/math_verify_leaderboard) for more details!

Normalizations can easily [be unfair if not designed well](https://huggingface.co/blog/open-llm-leaderboard-drop), but overall they still help provide signal at the task level.

They are also be important for evaluation of predictions generated with chain of thought, or reasoning, as you’ll need to remove the reasoning trace (which is not part of the final answer) from the output to get the actual answer.

#### [Sampling](https://openevals-evaluation-guidebook.hf.space/#sampling)

When models generate outputs, sampling multiple times and aggregating results can provide a more robust signal than a single greedy generation. This is particularly important for complex reasoning tasks where models may arrive at correct answers through different paths.

Common sampling-based metrics are:

- **pass@k over n**: Given n generated samples, measures whether at least k passes the test.
    
    You’ll find two functions for pass@k: computed trivially as: pass@k=(c>=k)pass@k=(c>=k), or computed with an unbiased estimator with: pass@k=1−(n−ck)(nk)pass@k=1−(kn​)(kn−c​)​ where c is the number of correct samples among n total samples.
    
- **maj@n** (majority voting): Sample n generations and take the most frequent answer. This helps filter out spurious outputs and works particularly well when the model’s correct reasoning path is more consistent than its errors. Commonly used for math and reasoning tasks.
    
- **cot@n** (chain-of-thought sampling): Sample n reasoning traces and evaluate them. Can be combined with majority voting or a pass@k (sample n reasoning chains, extract final answers, take majority or a threshold).
    
- **avg@n** (stable average score): Average the scores across n samples. It’s a more stable estimator of performance than using “best” or “most common” case.
    

Sampling metrics comparison

Question: What is 15 + 27?(Correct answer: 42)5 SAMPLED GENERATIONSSAMPLING METRICS

When you use sampling evaluations, make sure to always report all sampling parameters (temperature, top-p, k value) as they significantly affect results.

When can you use sampling and when shouldn't you?

- **For training evaluation/ablations**: ❌ Generally avoid sampling metrics as they’re expensive and add variance. Stick to greedy decoding with a fixed seed.
- **For post-training evaluation**: ✅ Sampling metrics can reveal capabilities that greedy decoding misses (especially for more complex tasks requiring reasoning, math or code).
- **At inference**: ✅ These metrics help estimate how much improvement you can get from sampling multiple times at inference. It’s particularly cool when you want to study how far you can push small models with test time compute.

However, keep in mind that sampling k times multiplies your evaluation cost by k. For expensive models or large datasets, this adds up very quickly!

#### [Functional scorers](https://openevals-evaluation-guidebook.hf.space/#functional-scorers)

Instead of comparing generated text to a reference through fuzzy string matching, functional testing evaluates whether outputs satisfy specific verifiable constraints. This approach is extremely promising because it’s more flexible and allows “infinite” updates of the test case through rule-based generation (which reduces overfitting).

**IFEval and IFBench** are excellent examples of this approach for instruction following evaluation. Rather than asking “does this text match a reference answer?”, they ask “does this text satisfy formatting constraints given in the instructions?”

For instance, instructions might specify:

- _“Include exactly 3 bullet points”_ → verify the output contains exactly 3 bullets
- _“Capitalize only the first sentence”_ → parse and check capitalization patterns
- _“Use the word ‘algorithm’ at least twice”_ → count word occurrences
- _“Your response must be in JSON format with keys ‘answer’ and ‘reasoning’”_ → validate JSON structure

Each constraint can be checked with a specific rule-based verifier, making these evaluations more unambiguous, interpretable, fast, and considerably less costly than using models as judges.

This functional approach works particularly well for instruction following, but requires creativity to extend to other text properties. The key is identifying aspects of text that can be verified programmatically rather than through semantic comparison.

Functional testing is inspired by code evaluation, where functional testing through unit tests is standard practice (checking if generated code produces correct outputs for given inputs).

### [With humans](https://openevals-evaluation-guidebook.hf.space/#with-humans)

Human evaluation is simply asking humans to score predictions.

Human evaluation is very interesting, because of its **flexibility** (if you define clearly enough what you are evaluating, you can get scores for about anything!), **inherent un-contamination** (if humans write new questions to test your system, they should not be present in your training data, hopefully), and **good correlation with human preference** for obvious reasons.

However, when doing evaluation with humans, you need to make sure your annotators are diverse enough that your results generalizes.

Different approaches exist to evaluate models with humans in the loop.

**Vibe-checks** is the name given to manual evaluations done by individual members of the community, usually on undisclosed prompts, to get an overall “feeling” of how well models perform on their use cases of preference. (I’ve also seen the term “canary-testing” used for this, in reference to high signal canary in a coalmine approach). Said use cases can be anything from the most exciting to the most mundate - to cite some I’ve seen on Reddit, they covered legal questions in German, coding, tool use, quality of erotica written, etc. Often shared on forums or social media, they mostly constitute anecdotal evidence, and tend to be highly sensitive to confirmation bias (in other words, people tend to find what they look for).

VIBE-CHECK EXAMPLESLetter CountingHow many "r"s in"strawberry"?Model A: 3✓Model B: 2✗Number ComparisonIs 9.9 bigger or smallerthan 9.11?Model A: 9.9 < 9.11✗Model B: 9.9 > 9.11✓Creative GenerationDraw a unicorn in TikZModel A: \draw[...] unicorn✓Model B: Error: invalid✗

Using community feedback to establish massive model rankings is what we call an **arena**. A well known example of this is the [LMSYS chatbot arena](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard), where community users are asked to chat with models until they find one is better than the other. Votes are then aggregated in an Elo ranking (a ranking of matches) to select which model is “the best”. The obvious problem of such an approach is the high subjectivity - it’s hard to enforce a consistent grading from many community members using broad guidelines, especially since annotators preferences tend to be [culturally bound](https://arxiv.org/abs/2404.16019v1) (with different people favoring different discussion topics, for example). One can hope that this effect is smoothed over by the sheer scale of the votes, through a “wisdom of the crowd” effect (this effect was found by a statistician named Galton, who observed that individual answers trying to estimate a numerical value, like the weight of a hog, could be modeled as a probability distribution centered around the actual answer).

The last approach is **systematic annotations**, where you provide extremely specific guidelines to paid selected annotators, in order to remove as much as the subjectivity bias as possible (this is the approach used by most data annotation companies). However, it can get extremely expensive fast, as you have to keep on doing evaluations in a continuous and non automatic manner for every new model you want to evaluate, and it can still fall prey to human bias (this [study](https://arxiv.org/abs/2205.00501) showed that people with different identities tend to rate model answer toxicity very differently).

Vibe-checks are a particularly [good starting point for your own use cases](https://olshansky.substack.com/p/vibe-checks-are-all-you-need), as you’ll be testing the model on what’s relevant to you. Pros of casual human evaluations are that they are cheap and allow to discover fun edge cases since you leverage user’s creativity in a mostly unbounded manner, you can discover interesting edge cases. However, they can be prone to blind spots.

For example, there was a debate in the scientific community as to whether LLMs [can draw](https://arxiv.org/abs/2303.12712) unicorns [or not](https://twitter.com/DimitrisPapail/status/1719119242186871275). A year later, seems like most can!

Once you want to scale to more systematic evaluation with paid annotators, you’ll find that there are 3 main ways to do so. If **you don’t have a dataset**, but want to explore a set of capabilities, you provide humans with a task and scoring guidelines (e.g _Try to make both these model output toxic language; a model gets 0 if it was toxic, 1 if it was not._), and access to one (or several) model(s) that they can interact with, then ask them to provide their scores and reasoning. If **you already have a dataset** (eg: a set of _prompts that you want your model to never answer_, for example for safety purposes), you preprompt your model with them, and provide the prompt, output and scoring guidelines to humans. If **you already have a dataset and scores**, you can ask humans to review your evaluation method by doing [error annotation](https://ehudreiter.com/2022/06/01/error-annotations-to-evaluate/) (_it can also be used as a scoring system in the above category_). It’s a very important step of testing new evaluation system, but it technically falls under evaluating an evaluation, so it’s slightly out of scope here.

Pros of systematic human evaluations, especially with paid annotators, are that you’re **getting high quality and private data** adapted to your use case (especially if you rely on in house annotators), which are mostly **explainable** (scores obtained by the models will be explainable by the humans who gave them). However, it’s more costly (especially as you’ll most likely need rounds of annotations to adapt your guidelines) and does not scale well.

Overall, however, human evaluation has a number of well known biases, based first impressions, tone, alignement with annotators value, etc, see the figure below.

HUMAN EVALUATION BIASESFirst ImpressionsQuality estimated from first impressions rather thanactual contentWell-formatted answer rated higher despite errorsarxiv.org/abs/2309.16349Tone BiasUnderestimation of the number of factual or logicalerrors in an assertive answerAssertive wrong answer > Neutral correct answerarxiv.org/abs/2309.16349Self-PreferencePreference for answers aligning with own views,opinons and beliefsPersonal beliefs > Factual correctnessarxiv.org/abs/2310.13548Identity BiasDifferent identity groups rate answers differentlyVaried toxicity ratings across demographicsarxiv.org/abs/2205.00501arxiv.org/abs/2404.16019

These biases are not unexpected, but they must be taken into account: not all use cases should rely on using cheap human annotators - any task requiring factuality (such as code writing, evaluation of model knowledge, etc) should include another, more robust, type of evaluation to complete the benchmark (experts, automatic metrics if applicable, etc).

### [With judge models](https://openevals-evaluation-guidebook.hf.space/#with-judge-models)

To mitigate the cost of human annotators, some people have looked into using models or derived artifacts (preferably aligned with human preferences) to evaluate models’ outputs.

This approach is not new, as you can find techniques to measure summarization quality from [model embeddings](https://arxiv.org/abs/1904.09675) in 2019.

Judge models are simply **neural network used to evaluate the output of other neural networks**. In most cases, they evaluate text generations.

Two approaches exist for grading: using [generalist, high capability models](https://arxiv.org/abs/2306.05685v4) or using [small specialist models](https://arxiv.org/pdf/2405.01535) trained specifically to discriminate from preference data (think “spam filter”, but for toxicity for example). In the former case, when using an LLM as a judge, you give it a prompt to explain how to score models (ex: `Score the fluency from 0 to 5, 0 being completely un-understandable, ...`).

Model as judges allow to score text on complex and nuanced properties. For example, an exact match between a prediction and reference can allow you to test if a model predicted the correct fact or number, but assessing more open-ended empirical capabilities (like fluency, poetry quality, or faithfulness to an input) requires more complex evaluators.

They are used on 3 main tasks:

- _Scoring a model generation_, on a provided scale, to assess a property of the text (fluency, toxicity, coherence, persuasiveness, etc).
- _Pairwise scoring_: comparing a pair model outputs to pick the best text with respect to a given property
- _Computing the similarity_ between a model output and a reference

In this document, I’ll focus on the LLMs + prompt approach for now, but you should definitely check out how classifier judges work, as I think it can be fairly robust and well adapted to a number of use cases, and the recently introduced and promising reward model as judge approach (introduced in [this tech report](https://research.nvidia.com/publication/2024-06_nemotron-4-340b), and on which we have a small page [here](https://github.com/huggingface/evaluation-guidebook/blob/main/contents/model-as-a-judge/what-about-reward-models.md))

#### [Pros and cons of using judge-LLMs](https://openevals-evaluation-guidebook.hf.space/#pros-and-cons-of-using-judge-llms)

People in favor of judge LLMs have been claiming they provide better:

- **Objectivity** when compared to humans: They automate empirical judgments in an objective and reproducible manner (theoretically - in my opinion, they add more subtle bias than they are worth)
- **Scale and reproducibility**: They are more scalable than human annotators, which allows to reproduce scoring on large amounts of data (if you control for temperature).
- **Cost**: They are cheap to instantiate, as they don’t require to train a new model, and can just rely on good prompting and an existing high quality LLM. They are also cheaper than paying actual human annotators (capitalism…).

In my opinion, using LLM judges correctly is extremely tricky, and it’s **easy to be deceived for critical use cases**:

- LLM as judges seem objective, but they have many **hidden biases** that can be harder to detect than the ones in humans, since we’re not as actively looking for them (see below). Besides, there are ways to reduce human bias by designing survey questions in specific and statistically robust ways (which has been studied in sociology for about a century), where LLM-prompting is not as robust yet. Using LLMs to evaluate LLMs has been compared to creating an echo-chamber effect, by reinforcing biases subtly.
- They are indeed scalable, but contribute to creating **massive amounts of data** which themselves need to be examined to ensure their quality (for example, you can improve the quality of LLM-judges by asking them to generate a thinking trace, or reasoning around their data, which makes even more new artificial data to analyse)
- They are indeed cheap to instantiate, but are not as good as paying actual expert human annotators for your specific use cases.

LLM JUDGE BIASESNo Internal ConsistencyGives different judgements if prompted multipletimes (at T>0)No Consistent Score RangesModel ranking do not follow a consistent scale (e.g:for a task where scores should be 1, 2, 3, 4, ... 10, themodel might score 1, 1, 1, 10, 10 ... 10)x.com/aparnadhinak/status/1748368364395721128github.com/LeonEricsson/llmjudgeSelf-PreferenceJudge will favor outputs from similar models whenscoringarxiv.org/abs/2404.13076Blindness to Input PerturbationIf input is perturbed, judges don't detect qualitydrops consistentlyarxiv.org/abs/2406.13439Position BiasWhen comparing answers, judge favors specificanswer positions (e.g: systematically prefers first orsecond choice)arxiv.org/abs/2306.05685Verbosity BiasModels prefer more verbose answersarxiv.org/abs/2404.04475No Consistency With Human ScoringLLM ratings diverge from human ratingsarxiv.org/abs/2308.15812Format BiasJudge can't judge well when their prompt differs fromtheir training prompt formatarxiv.org/abs/2310.17631

This section is therefore a bit long, because you need to be well aware of the limitations of using model as judges: a lot of people are blindly jumping into using them because they seem easier than actually working with humans or designing new metrics, but then end up with uninsterpretable data with tricky bias to extract.

My main personal gripe with using models as judges is that they introduce very subtle and un-interpretable bias in the answer selection. I feel that, much like when crossbreeding too much in genetics studies, you end up with dysfunctional animals or plants, by using LLMs to select and train LLMs, we are just as likely to introduce minute changes that will have bigger repercussions a couple generations down the line. I believe this type of bias is less likely to occur in smaller and more specialized models as judges (such as toxicity classifiers), but this remains to be rigorously tested and proven.

Getting started with an LLM judge

If you want to give it a go, I suggest first reading this [very good guide](https://huggingface.co/learn/cookbook/en/llm_judge) on how to setup your first LLM as judge!

You can also try the [distilabel](https://distilabel.argilla.io/latest/) library, which allows you to generate synthetic data and update it using LLMs. They have a nice [tutorial](https://distilabel.argilla.io/latest/sections/pipeline_samples/papers/ultrafeedback/) applying the methodology of the [Ultrafeedback paper](https://arxiv.org/abs/2310.01377) as well as a [tutorial on benchmarking](https://distilabel.argilla.io/latest/sections/pipeline_samples/examples/benchmarking_with_distilabel/) implementing the Arena Hard benchmark.

#### [Getting a Judge-Model](https://openevals-evaluation-guidebook.hf.space/#getting-a-judge-model)

When using an existing LLM, you can go for [generalist, high capability models](https://arxiv.org/abs/2306.05685v4), [small specialist models](https://arxiv.org/abs/2405.01535) trained specifically to discriminate from preference data, or training your own.

**Using a generalist LLM**

With the introduction of more capable LLMs (such as ChatGPT), some researchers started exploring using big models as judges.

⚖️

Closed vs open source judge models

**Closed source models (Claude, GPT-o) tradeoffs:**

Disadvantages:

- **Non-reproducible**: Models can change without notice via API updates
- **Black box**: Un-interpretable decision-making
- **Privacy risks**: Data sent to third parties, potential leakage

Advantages:

- Easy access without local setup or hardware requirements

**Open source models are closing the gap** while solving reproducibility and interpretability issues. Models like DeepSeek R1, gpt-oss, and the recent Qwen models are now competitive alternatives.

You’ll find a good cost analysis of model providers [here](https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard) if you need help picking one.

**Using a tiny specialized LLM judge model**

You can also make the choice to use tiny specialized LLM judges. With often a couple billion parameters, they can run locally on most recent consumer hardware, while being trained from scratch or fine-tuned using instruction data. You often need to follow their specific prompt formats.

Some existing models as of 2024 were Flow-Judge-v0.1 ([weights](https://huggingface.co/collections/flowaicom/flow-judge-v01-66e6af5fc3b3a128bde07dec)), 3.8B parameters, a Phi-3.5-mini-instruct fine-tuned on a synthetic preference dataset, Prometheus ([weights](https://huggingface.co/prometheus-eval/prometheus-13b-v1.0), [paper](https://arxiv.org/abs/2310.08491)), 13B parameters, a model trained from scratch on synthetic preference dataset, and JudgeLM ([paper](https://arxiv.org/abs/2310.17631)), 7B to 33B parameters, models trained from scratch on synthetic preference datasets generated with a variety of models. Newer alternatives surely exist!

**Training your own** You can also make the choice to train or fine-tune your own LLM-as-judge. (I would avoid doing this, unless you are on a very niche domain).

If you go in that direction, you’ll first need to gather preference data for your task of interest, which can come

- From existing [human preference datasets](https://www.kaggle.com/competitions/lmsys-chatbot-arena)
- From model generated preference data (which you can generate following the above tiny-model judges papers data sections, or get directly, for example from the Prometheus [preference](https://huggingface.co/datasets/prometheus-eval/Preference-Collection) and [feedback](https://huggingface.co/datasets/prometheus-eval/Feedback-Collection) collections).

Then you need to decide whether to start from a small model to train from scratch, or from an existing model, that you can distill into a new smaller model, or quantize, then fine-tune (using peft or adapter weights if the model is big and your training compute low) using the above data.

Apparently [starting from a reward model works better than from an instruct model](https://x.com/dk21/status/1826292289930674590)

#### [Designing your evaluation prompt](https://openevals-evaluation-guidebook.hf.space/#designing-your-evaluation-prompt)

Once you’ve selected your model, you need to define what is the best possible prompt for your task.

📝

Prompt design guidelines

Provide a clear description of the task at hand:

- _Your task is to do X._
- _You will be provided with Y._

Provide clear instructions on the evaluation criteria, including a detailed scoring system if needed:

- _You should evaluate property Z on a scale of 1 - 5, where 1 means …_
- _You should evaluate if property Z is present in the sample Y. Property Z is present if …_

Provide some additional “reasoning” evaluation steps:

- _To judge this task, you must first make sure to read sample Y carefully to identify …, then …_

Specify the desired output format (adding fields will help consistency)

- _Your answer should be provided in JSON, with the following format {“Score”: Your score, “Reasoning”: The reasoning which led you to this score}_

You can and should take inspiration from [MixEval](https://github.com/huggingface/lighteval/blob/main/src/lighteval/tasks/extended/mix_eval/judge_prompts.pyy) or [MTBench](https://github.com/huggingface/lighteval/blob/main/src/lighteval/tasks/extended/mt_bench/judge_prompt_templates.py) prompt templates.

⚠️

To remember when doing model as judge

Pairwise comparison [correlates better with human preference](https://arxiv.org/abs/2403.16950) than scoring, and is more robust generally.

If you really want a score, use an integer scale make sure you provide a detailed explanation for what [each score represents](https://x.com/seungonekim/status/1749289437165769177), or an additive prompt (_provide 1 point for this characteristic of the answer, 1 additional point if …_ etc)

Using one prompt per capability to score tends to give better and more robust results

You can also improve accuracy using the following, possibly more costly, techniques:

- **Few shot examples**: like in many other tasks, if you provide examples it can help its reasoning. However, this adds to your context length.
- **Reference**: you can also enhance your prompt with a reference if present, which increases accuracy
- **CoT**: [improves accuracy for older gen models](https://arxiv.org/abs/2212.08073), if you ask the model to output its chain of thought **before** the score (also observed [here](https://x.com/seungonekim/status/1749289437165769177))
- **Multiturn analysis**: can improve [factual error detection](https://arxiv.org/abs/2305.13281)
- Using **a jury** (many judges, where you pick an aggregate of the answers): [gives better results](https://arxiv.org/abs/2404.18796) than using a single model. It can be made considerably less costly by leveraging many smaller models instead of one big expensive model. You can also experiment with using one model with variations on temperature
- Surprisingly, the community has found that adding stakes to the prompts (`answer correctly and you'll get a kitten`) can increase correctness. Your mileage may vary on this one, adapt to your needs.

If you are working on critical tasks (medical domain for example), make sure to use methodologies transferred from the humanities, and 1) compute inter-annotator agreement metrics to make sure your evaluators are as unbiased as possible, 2) Use proper survey design methodology when creating your scoring grid to mitigate bias. However, most people don’t really want a reproducible and high quality unbiased eval, and will be happy with quick and dirty evaluation through OK-ish prompts. (Which is an OK situation to be in! Just depends on the consequences attached).

#### [Evaluating your evaluator](https://openevals-evaluation-guidebook.hf.space/#evaluating-your-evaluator)

Before using a judge-LLM in production or at scale, you want to evaluate its quality for your task, to make sure its scores are actually relevant and useful for you.

This will be easier to do if it predicts binary outputs, because you’ll be able to interpretable classification metrics (accuracy/recall/precision). If it predicts scores on a scale, it will be much harder to estimate the quality of the correlation with a reference. Models are notoriously bad at predicting on a scale.

So, once you have selected your model judge and its prompt, you’ll need to do the following.

1. **Pick your baseline** You’ll need to compare your evaluator judgments to a baseline: it can be human annotations, the output of another judge model that you know is qualitative on your task, a gold truth, itself with another prompt, etc.

🎯

Quality over quantity for baseline

You don’t need many baseline examples (50 can suffice), but they must be:

- **Representative**: Cover the full range of your task
- **Discriminative**: Include edge cases and challenging examples
- **High quality**: Use the best reference data you can obtain

2. **Pick your metric** Your metric will be used to compare your judge’s evaluations with your reference.

In general, this comparison is considerably easier to do if your model is predicting binary classes or doing pairwise comparison, as you’ll be able to compute accuracy (for pairwise comparison), or precision and recall (for binary classes), which are all very easy to interpret metrics.

Comparing the correlation of scores with human or model scoring will be harder to do. To understand why in more detail, I advise you to read this cool [blog section on the topic](https://eugeneyan.com/writing/llm-evaluators/#key-considerations-before-adopting-an-llm-evaluator).

In general, if you’re a bit lost about what metrics to pick when (in terms of models, metrics, …), you can also look at [this interesting graph](https://eugeneyan.com/assets/llm-eval-tree.jpg) from [the same above blog](https://eugeneyan.com/writing/llm-evaluators/) ⭐.

3. **Evaluate your evaluator** For this step, you simply need to use your model and its prompt to evaluate your test samples! Then, once you get the evaluations, use your above metric and reference to compute a score for your evaluations.

You need to decide what your threshold for acceptance is. Depending on how hard your task is, you can aim for 80% to 95% accuracy, if you’re doing pairwise comparison. Regarding correlations (if you’re using scores), people in the literature tend to seem happy with 0.8 Pearson correlation with a reference. However, I’ve seen some papers declare that 0.3 indicates a good correlation with human annotators (^^”) so ymmv.

#### [Tips and tricks](https://openevals-evaluation-guidebook.hf.space/#tips-and-tricks)

⚠️

Mitigating well known biases of LLM as judges

We discussed in this section’s [intro](http://localhost:4321/#pros-and-cons-of-using-judge-llms) a number of LLM judges biases. Let’s see how you should try to mitigate them.

**Lack of internal consistency**: ➡️ You can mitigate this by doing self-consistency prompting of your judge, prompting it multiple times and keeping the majority output

**Self-preference**: ➡️ You can mitigate this by using a jury

**Blindness to input perturbation**: ➡️ asking the model to explain its reasoning [before providing a score](https://twitter.com/seungonekim/status/1749289437165769177) ➡️ or providing a coherent grading scale in the prompt.

**Position-bias**: ➡️ switching answer positions randomly ➡️ computing the log-probabilities of all possible choices to get a normalized answer

**Verbosity-bias** (or length-bias): ➡️ You can mitigate this by [accounting for the answer difference in length](https://arxiv.org/abs/2404.04475)

**Format bias**: ➡️ You can mitigate this by paying attention to the training prompt format (if the model was instruction tuned) and ensuring you follow it.

**Picking correct tasks for an LLM judge**

LLM evaluators:

- are **bad at identifying hallucinations** in general, particularly what are called partial hallucinations (which look close to the ground truth but are actually slightly different) (see [this](https://arxiv.org/abs/2305.11747) and [this](https://arxiv.org/abs/2303.08896))
- have a low to OK-ish correlation with human annotators on [summarization](https://arxiv.org/abs/2304.02554) ([here too](https://arxiv.org/abs/2303.16634)), [faithfulness](https://arxiv.org/abs/2307.16877), and are not consistently correlated with human judgement more broadly against [a scope of tasks](https://arxiv.org/abs/2406.18403)

#### [What about Reward Models?](https://openevals-evaluation-guidebook.hf.space/#what-about-reward-models)

Reward models learn to predict a score from human annotations for given prompt/completion pairs. The end goal is for them to do predictions aligned with human preference. Once trained, these models can then be used to improve other models, by acting as a a reward function which is a proxy for human judgment.

The most common type of reward model is the Bradley-Terry model, which outputs a single **pairwise score**, following:

p(completion b is better than completion a)=sigmoid(scoreb−scorea)p(completion b is better than completion a)=sigmoid(scoreb​−scorea​)

This model is trained using only pairwise comparisons of completions, which are easier to collect than scores, but can only compare several completions for one prompt, and not completions across prompts.

Other models have expanded on this approach to predict a more nuanced probability that a completion is better than the other one ([example](https://huggingface.co/RLHFlow/pair-preference-model-LLaMA3-8B)).

This allows them to (theoretically) judge subtle differences between completions, at the cost of not being able to easily save and compare many different scores across prompts for the same test set. In addition, context length and memory limits can become an issue when comparing too long completions.

Some reward models such as [SteerLM](https://arxiv.org/abs/2311.09528) output **absolute scores**, which can be used to evaluate completions directly without the need for pairwise comparisions. These models can be easier to use for evaluation, but are also harder to collect data for, as absolute scores tend to be less stable than pairwise scores in human preferences.

More recently, models have been proposed that output both absolute and relative scores, such as [HelpSteer2-Preference](https://arxiv.org/abs/2410.01257) and [ArmoRM](https://arxiv.org/abs/2406.12845).

How do I use a Reward Model for Evaluation?

Given a dataset of prompts, we can generate completions from a language model and ask a reward model to score them.

For models that give absolute scores, the resulting scores can be averaged to get a reasonable summary score.

However, in the more common case of relative scores, the average reward can be biased by outliers (a few very good or very bad completions) as different prompts may have inherently different reward scales (some prompts are way harder or easier than others).

For relative scores, don’t just average raw rewards—outliers and varying prompt difficulty scales will bias results. Use win rates or win probabilities against a reference instead.

Instead, we can use

- win rates: take a reference set of completions and calculate the percentage of completions from the model that are ranked higher than the reference completions. It is slightly more granular.
- win probabilities: the mean probability of the completions being better than the reference completions, which can give a more fine-grained and smoothly changing signal.

Pros and Cons of Reward Models

Reward models are typically:

- **Very fast**: Getting a score is as simple as running a forward pass of a relatively small model once (since we only get a score, and not long text, contrary to judge-LLMs)
- **Deterministic**: The same scores will be reproduced through the same forward pass
- **Unlikely to suffer from positional bias**: As most models take only one completion, they can not be influenced by the order. For pairwise models, positional bias is often also minimal, as long as the training data was balanced with respect to containing both first and second answers as being the best.
- **Require no prompt engineering**: since the model will simply output a score from one or two completions depending on preference data it’s been trained on.

On the other hand they:

- **Require specific fine-tuning**: This can be a relatively costly step, and elthough they inherit many capabilities from a base model, they may still perform poorly on tasks that are out of the training distribution.
- **Loose efficiency when used both in reinforcement learning and evaluation** (or when using direct alignment algorithms on datasets that are similar to the training data of the reward model), as the language model may overfit to the reward model’s preferences.

Going further

- A good place to find high performing models is the [RewardBench Leaderboard](https://huggingface.co/spaces/allenai/reward-bench).
- You can look at how reward models have been used in the [Nemotron](https://arxiv.org/abs/2406.11704) paper.
- For reward models that rate single prompts and completions, you can cache the scores of many reference models and easily see how a new model performs.
- Tracking of win rates or probabilities over training, e.g. as in [this](https://arxiv.org/abs/2410.11677v1) paper, can allow you to detect model degradation and select optimal checkpoints.

### [Constraining model outputs](https://openevals-evaluation-guidebook.hf.space/#constraining-model-outputs)

In a number of cases, we might want the model to output a prediction which follows a very specific format to simplify evaluation.

#### [Using a prompt](https://openevals-evaluation-guidebook.hf.space/#using-a-prompt)

The easiest way to do this is to add a task prompt which contains very specific instructions as to how the model should answer (`Provide numerical answers in digits.`,`Use no abbreviation.`, etc).

It won’t necessarily work all the time but should be good enough for high capability models. That’s the approach we followed in the [GAIA](https://huggingface.co/papers/2311.12983) paper for example.

#### [Few shots and in context learning](https://openevals-evaluation-guidebook.hf.space/#few-shots-and-in-context-learning)

The next way to do so is to constrain the model through what is called “in context learning”. By providing examples in the prompt (what is called `few-shot prompting`), the model is implicitly biased towards following the repeated prompt shape for the actual sample.

It’s a method which was overall working quite well until end of 2023!

However, the widespread adoption of instruction-tuning methods and the addition of instruction data in later stages of model pre-training (continuous pre-training) has biased more recent models towards specific output formats (what is being called [here](https://arxiv.org/abs/2407.07890) _Training on the test task_, and what I would call _overfitting the prompt format_). Reasoning models are also not playing that well with few shot examples because of the reasoning trace.

It’s also a method which can be limited for older models with smaller context sizes, as some few-shot examples can not fit into the context window.

#### [Structured text generation](https://openevals-evaluation-guidebook.hf.space/#structured-text-generation)

Structured text generation constrains the outputs to follow a given path, defined by a grammar or by regular expressions, for example. The `outlines` library implements this using finite state machines, which is very neat. (Other approaches exist, such as using interleaved generation for json generation, but the FSM one is my favorite).

To understand more about what happens when using structured generation, you can check the [blog](https://huggingface.co/blog/evaluation-structured-outputs) we wrote together: structured generation reduce prompt variance in evaluation, and make results and rankings more stable. You can also check the overall `outlines` [blog](https://blog.dottxt.co/) for interesting implementations and observations linked to structured generation.

However, some recent [research](https://arxiv.org/abs/2408.02442) seems to show that structured generation can lower model performance on some tasks (like reasoning), by moving the prior too far away from the expected probability distribution.

📚

Going further

- ⭐ [Understanding how Finite State Machine when using structured generation](https://blog.dottxt.co/coalescence.html), by Outlines. Super clear guide on how their method works!
- [The outlines method paper](https://arxiv.org/abs/2307.09702), a more academic explanation of the above
- [Interleaved generation](https://github.com/guidance-ai/guidance?tab=readme-ov-file#guidance-acceleration), another method to constrain generations for some specific output formats

## [The forgotten children of evaluation](https://openevals-evaluation-guidebook.hf.space/#the-forgotten-children-of-evaluation)

### [Statistical validity](https://openevals-evaluation-guidebook.hf.space/#statistical-validity)

When reporting evaluation results, it’s critical to include **confidence intervals** alongside point estimates.

These confidence intervals from the raw scores can be obtained from standard deviations over the scores or [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_\(statistics\)) - for automatic metrics, this is relatively trivial - for model judges, a [recent paper](https://arxiv.org/pdf/2511.21140) suggested bias correction with estimators. For human based evaluations, you should report agreement.

You can also compute these with prompt variations, by asking the same questions in slightly different ways, or re-running on the same samples with different prompt formats.

### [Cost and efficiency](https://openevals-evaluation-guidebook.hf.space/#cost-and-efficiency)

When designing and reporting evaluation results, we need to start collectively reporting results against model running costs! A reasoning model which requires 10 minutes of thinking and 10K tokens to answer 10 + 1 (because it decides to make an entire segue on binary vs decimal arithmetics) is considerably less efficient than a smol model answering 30 in a handful of tokens.

![Environmental impact metrics for model evaluation](https://openevals-evaluation-guidebook.hf.space/_astro/env.CeZN1NHy.png)

We suggest you report the following:

- **Token consumption**: Report the total number of output tokens used during evaluation. This is particularly important to estimate **efficiency**, and it will affect the cost of model as judge evaluations. Token counts directly impact monetary costs and help others estimate the computational requirements. **Monetary cost** can also be a good proxy for efficiency.

These cost metrics can also be critical when comparing evaluation methods. For instance, while using a powerful LLM as a judge might provide better signal than automatic metrics, the 100x cost increase may not be justified for all use cases. Similarly, sampling-based metrics (pass@k, maj@n) multiply costs with the number of samples, which should be weighed against the improved signal they provide.

- **Time**: Document the inference time required by the model to complete the evaluation. This includes both the actual inference time and any overhead from API rate limits. This is particularly important for any time-sensitive applications (like some agentic tool use, as in GAIA2).

Last but not least, reporting the environmental footprint of the models you are running is becoming increasingly important with the overall state of resources available on earth. This includes carbon emissions from training and energy consumption at inference, and these will depend on the model size, hardware (if you know it) and the tokens generated. Some smaller or quantized models reach a very interesting performance to consumption ratio

## [Conclusion](https://openevals-evaluation-guidebook.hf.space/#conclusion)

Evaluation is both an art and a science. We’ve explored the landscape of LLM evaluation in 2025—from understanding why we evaluate models and the fundamental mechanics of tokenization and inference, to navigating the ever-evolving ecosystem of benchmarks, and finally to creating evaluations for your own use-cases.

Key things I hope you’ll remember are:

**Think critically about what you’re measuring.** Evaluations are proxies for capabilities, so a high score on a benchmark doesn’t guarantee real-world performance. Different evaluation approaches (automatic metrics, human judges, or model judges) each come with their own biases, limitations, and tradeoffs.

**Match your evaluation to your goal.** Are you running ablations during training? Use fast, reliable benchmarks with strong signal even on small models. Comparing final models for selection? Focus on harder, uncontaminated datasets that test holistic capabilities. Building for a specific use case? Create custom evaluations that reflect your problems and data.

**Reproducibility requires attention to detail.** Small differences in prompts, tokenization, normalization, templates, or random seeds can swing scores by several points. When reporting results, be transparent about your methodology. When trying to reproduce results, expect that exact replication will be extremely challenging even if you attempt to control for every variable.

**Prefer interpretable evaluation methods.** When possible, functional testing and rule-based verifiers should be chosen over model judges. Evaluations that can be understood and debugged will provide clearer and more actionable insights… and the more interpretable your evaluation, the more you can improve your models!

**Evaluation is never finished.** As models improve, benchmarks saturate. As training data grows, contamination becomes more likely. As use cases evolve, new capabilities need measuring. Evaluation is an ongoing battle!

To conclude: The models we build are only as good as our ability to measure what matters. Thanks for reading!

### [Acknowledgments](https://openevals-evaluation-guidebook.hf.space/#acknowledgments)

Many thanks to all the people who contributed directly or indirectly to this document, notably Hynek Kydlicek, Loubna Ben Allal, Sander Land and Nathan Habib.

### Citation

For attribution in academic contexts, please cite this work as

Clémentine Fourrier, Thibaud Frere, Guilherme Penedo, Thomas Wolf (2025). "The LLM Evaluation Guidebook".

BibTeX citation

@misc{fourrier2025_the_llm_evaluation_guidebook,
  title={The LLM Evaluation Guidebook},
  author={Clémentine Fourrier and Thibaud Frere and Guilherme Penedo and Thomas Wolf},
  year={2025},
  
}

Made with ❤️ with [research article template](https://huggingface.co/spaces/tfrere/research-article-template)