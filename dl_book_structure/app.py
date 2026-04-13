import os
from flask import Flask, render_template

app = Flask(__name__)

BOOK = {
    "title": "Deep Learning",
    "authors": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
    "year": 2016,
    "publisher": "MIT Press",
    "url": "https://www.deeplearningbook.org/",
    "front": ["Acknowledgements", "Notation"],
    "parts": [
        {
            "name": "Part 0 — Introduction",
            "chapters": [
                {
                    "num": 1, "title": "Introduction",
                    "sections": [
                        ("1.1", "Who Should Read This Book?", []),
                        ("1.2", "Historical Trends in Deep Learning", [
                            "1.2.1 The Many Names and Changing Fortunes of Neural Networks",
                            "1.2.2 Increasing Dataset Sizes",
                            "1.2.3 Increasing Model Sizes",
                            "1.2.4 Increasing Accuracy, Complexity, and Real-World Impact",
                        ]),
                    ],
                },
            ],
        },
        {
            "name": "Part I — Applied Math and Machine Learning Basics",
            "chapters": [
                {
                    "num": 2, "title": "Linear Algebra",
                    "sections": [
                        ("2.1", "Scalars, Vectors, Matrices and Tensors", []),
                        ("2.2", "Multiplying Matrices and Vectors", []),
                        ("2.3", "Identity and Inverse Matrices", []),
                        ("2.4", "Linear Dependence and Span", []),
                        ("2.5", "Norms", []),
                        ("2.6", "Special Kinds of Matrices and Vectors", []),
                        ("2.7", "Eigendecomposition", []),
                        ("2.8", "Singular Value Decomposition", []),
                        ("2.9", "The Moore-Penrose Pseudoinverse", []),
                        ("2.10", "The Trace Operator", []),
                        ("2.11", "The Determinant", []),
                        ("2.12", "Example: Principal Components Analysis", []),
                    ],
                },
                {
                    "num": 3, "title": "Probability and Information Theory",
                    "sections": [
                        ("3.1", "Why Probability?", []),
                        ("3.2", "Random Variables", []),
                        ("3.3", "Probability Distributions", [
                            "3.3.1 Discrete Variables and Probability Mass Functions",
                            "3.3.2 Continuous Variables and Probability Density Functions",
                        ]),
                        ("3.4", "Marginal Probability", []),
                        ("3.5", "Conditional Probability", []),
                        ("3.6", "The Chain Rule of Conditional Probabilities", []),
                        ("3.7", "Independence and Conditional Independence", []),
                        ("3.8", "Expectation, Variance and Covariance", []),
                        ("3.9", "Common Probability Distributions", [
                            "3.9.1 Bernoulli Distribution",
                            "3.9.2 Multinoulli Distribution",
                            "3.9.3 Gaussian Distribution",
                            "3.9.4 Exponential and Laplace Distributions",
                            "3.9.5 The Dirac Distribution and Empirical Distribution",
                            "3.9.6 Mixtures of Distributions",
                        ]),
                        ("3.10", "Useful Properties of Common Functions", []),
                        ("3.11", "Bayes' Rule", []),
                        ("3.12", "Technical Details of Continuous Variables", []),
                        ("3.13", "Information Theory", []),
                        ("3.14", "Structured Probabilistic Models", []),
                    ],
                },
                {
                    "num": 4, "title": "Numerical Computation",
                    "sections": [
                        ("4.1", "Overflow and Underflow", []),
                        ("4.2", "Poor Conditioning", []),
                        ("4.3", "Gradient-Based Optimization", [
                            "4.3.1 Beyond the Gradient: Jacobian and Hessian Matrices",
                        ]),
                        ("4.4", "Constrained Optimization", []),
                        ("4.5", "Example: Linear Least Squares", []),
                    ],
                },
                {
                    "num": 5, "title": "Machine Learning Basics",
                    "sections": [
                        ("5.1", "Learning Algorithms", [
                            "5.1.1 The Task, T",
                            "5.1.2 The Performance Measure, P",
                            "5.1.3 The Experience, E",
                            "5.1.4 Example: Linear Regression",
                        ]),
                        ("5.2", "Capacity, Overfitting and Underfitting", [
                            "5.2.1 The No Free Lunch Theorem",
                            "5.2.2 Regularization",
                        ]),
                        ("5.3", "Hyperparameters and Validation Sets", [
                            "5.3.1 Cross-Validation",
                        ]),
                        ("5.4", "Estimators, Bias and Variance", [
                            "5.4.1 Point Estimation",
                            "5.4.2 Bias",
                            "5.4.3 Variance and Standard Error",
                            "5.4.4 Trading off Bias and Variance to Minimize MSE",
                            "5.4.5 Consistency",
                        ]),
                        ("5.5", "Maximum Likelihood Estimation", [
                            "5.5.1 Conditional Log-Likelihood and Mean Squared Error",
                            "5.5.2 Properties of Maximum Likelihood",
                        ]),
                        ("5.6", "Bayesian Statistics", [
                            "5.6.1 Maximum A Posteriori (MAP) Estimation",
                        ]),
                        ("5.7", "Supervised Learning Algorithms", [
                            "5.7.1 Probabilistic Supervised Learning",
                            "5.7.2 Support Vector Machines",
                            "5.7.3 Other Simple Supervised Learning Algorithms",
                        ]),
                        ("5.8", "Unsupervised Learning Algorithms", [
                            "5.8.1 Principal Components Analysis",
                            "5.8.2 k-means Clustering",
                        ]),
                        ("5.9", "Stochastic Gradient Descent", []),
                        ("5.10", "Building a Machine Learning Algorithm", []),
                        ("5.11", "Challenges Motivating Deep Learning", [
                            "5.11.1 The Curse of Dimensionality",
                            "5.11.2 Local Constancy and Smoothness Regularization",
                            "5.11.3 Manifold Learning",
                        ]),
                    ],
                },
            ],
        },
        {
            "name": "Part II — Modern Practical Deep Networks",
            "chapters": [
                {
                    "num": 6, "title": "Deep Feedforward Networks",
                    "sections": [
                        ("6.1", "Example: Learning XOR", []),
                        ("6.2", "Gradient-Based Learning", [
                            "6.2.1 Cost Functions",
                            "6.2.2 Output Units",
                        ]),
                        ("6.3", "Hidden Units", [
                            "6.3.1 Rectified Linear Units and Their Generalizations",
                            "6.3.2 Logistic Sigmoid and Hyperbolic Tangent",
                            "6.3.3 Other Hidden Units",
                        ]),
                        ("6.4", "Architecture Design", [
                            "6.4.1 Universal Approximation Properties and Depth",
                            "6.4.2 Other Architectural Considerations",
                        ]),
                        ("6.5", "Back-Propagation and Other Differentiation Algorithms", [
                            "6.5.1 Computational Graphs",
                            "6.5.2 Chain Rule of Calculus",
                            "6.5.3 Recursively Applying the Chain Rule to Obtain Backprop",
                            "6.5.4 Back-Propagation Computation in Fully-Connected MLP",
                            "6.5.5 Symbol-to-Symbol Derivatives",
                            "6.5.6 General Back-Propagation",
                            "6.5.7 Example: Back-Propagation for MLP Training",
                            "6.5.8 Complications",
                            "6.5.9 Differentiation outside the Deep Learning Community",
                            "6.5.10 Higher-Order Derivatives",
                        ]),
                        ("6.6", "Historical Notes", []),
                    ],
                },
                {
                    "num": 7, "title": "Regularization for Deep Learning",
                    "sections": [
                        ("7.1", "Parameter Norm Penalties", [
                            "7.1.1 L2 Parameter Regularization",
                            "7.1.2 L1 Regularization",
                        ]),
                        ("7.2", "Norm Penalties as Constrained Optimization", []),
                        ("7.3", "Regularization and Under-Constrained Problems", []),
                        ("7.4", "Dataset Augmentation", []),
                        ("7.5", "Noise Robustness", ["7.5.1 Injecting Noise at the Output Targets"]),
                        ("7.6", "Semi-Supervised Learning", []),
                        ("7.7", "Multi-Task Learning", []),
                        ("7.8", "Early Stopping", []),
                        ("7.9", "Parameter Tying and Parameter Sharing", ["7.9.1 Convolutional Neural Networks"]),
                        ("7.10", "Sparse Representations", []),
                        ("7.11", "Bagging and Other Ensemble Methods", []),
                        ("7.12", "Dropout", []),
                        ("7.13", "Adversarial Training", []),
                        ("7.14", "Tangent Distance, Tangent Prop, and Manifold Tangent Classifier", []),
                    ],
                },
                {
                    "num": 8, "title": "Optimization for Training Deep Models",
                    "sections": [
                        ("8.1", "How Learning Differs from Pure Optimization", [
                            "8.1.1 Empirical Risk Minimization",
                            "8.1.2 Surrogate Loss Functions and Early Stopping",
                            "8.1.3 Batch and Minibatch Algorithms",
                        ]),
                        ("8.2", "Challenges in Neural Network Optimization", [
                            "8.2.1 Ill-Conditioning",
                            "8.2.2 Local Minima",
                            "8.2.3 Plateaus, Saddle Points and Other Flat Regions",
                            "8.2.4 Cliffs and Exploding Gradients",
                            "8.2.5 Long-Term Dependencies",
                            "8.2.6 Inexact Gradients",
                            "8.2.7 Poor Correspondence between Local and Global Structure",
                            "8.2.8 Theoretical Limits of Optimization",
                        ]),
                        ("8.3", "Basic Algorithms", [
                            "8.3.1 Stochastic Gradient Descent",
                            "8.3.2 Momentum",
                            "8.3.3 Nesterov Momentum",
                        ]),
                        ("8.4", "Parameter Initialization Strategies", []),
                        ("8.5", "Algorithms with Adaptive Learning Rates", [
                            "8.5.1 AdaGrad",
                            "8.5.2 RMSProp",
                            "8.5.3 Adam",
                            "8.5.4 Choosing the Right Optimization Algorithm",
                        ]),
                        ("8.6", "Approximate Second-Order Methods", [
                            "8.6.1 Newton's Method",
                            "8.6.2 Conjugate Gradients",
                            "8.6.3 BFGS",
                        ]),
                        ("8.7", "Optimization Strategies and Meta-Algorithms", [
                            "8.7.1 Batch Normalization",
                            "8.7.2 Coordinate Descent",
                            "8.7.3 Polyak Averaging",
                            "8.7.4 Supervised Pretraining",
                            "8.7.5 Designing Models to Aid Optimization",
                            "8.7.6 Continuation Methods and Curriculum Learning",
                        ]),
                    ],
                },
                {
                    "num": 9, "title": "Convolutional Networks",
                    "sections": [
                        ("9.1", "The Convolution Operation", []),
                        ("9.2", "Motivation", []),
                        ("9.3", "Pooling", []),
                        ("9.4", "Convolution and Pooling as an Infinitely Strong Prior", []),
                        ("9.5", "Variants of the Basic Convolution Function", []),
                        ("9.6", "Structured Outputs", []),
                        ("9.7", "Data Types", []),
                        ("9.8", "Efficient Convolution Algorithms", []),
                        ("9.9", "Random or Unsupervised Features", []),
                        ("9.10", "The Neuroscientific Basis for Convolutional Networks", []),
                        ("9.11", "Convolutional Networks and the History of Deep Learning", []),
                    ],
                },
                {
                    "num": 10, "title": "Sequence Modeling: Recurrent and Recursive Nets",
                    "sections": [
                        ("10.1", "Unfolding Computational Graphs", []),
                        ("10.2", "Recurrent Neural Networks", [
                            "10.2.1 Teacher Forcing and Networks with Output Recurrence",
                            "10.2.2 Computing the Gradient in a Recurrent Neural Network",
                            "10.2.3 Recurrent Networks as Directed Graphical Models",
                            "10.2.4 Modeling Sequences Conditioned on Context with RNNs",
                        ]),
                        ("10.3", "Bidirectional RNNs", []),
                        ("10.4", "Encoder-Decoder Sequence-to-Sequence Architectures", []),
                        ("10.5", "Deep Recurrent Networks", []),
                        ("10.6", "Recursive Neural Networks", []),
                        ("10.7", "The Challenge of Long-Term Dependencies", []),
                        ("10.8", "Echo State Networks", []),
                        ("10.9", "Leaky Units and Other Strategies for Multiple Time Scales", [
                            "10.9.1 Adding Skip Connections through Time",
                            "10.9.2 Leaky Units and a Spectrum of Different Time Scales",
                            "10.9.3 Removing Connections",
                        ]),
                        ("10.10", "The Long Short-Term Memory and Other Gated RNNs", [
                            "10.10.1 LSTM",
                            "10.10.2 Other Gated RNNs",
                        ]),
                        ("10.11", "Optimization for Long-Term Dependencies", [
                            "10.11.1 Clipping Gradients",
                            "10.11.2 Regularizing to Encourage Information Flow",
                        ]),
                        ("10.12", "Explicit Memory", []),
                    ],
                },
                {
                    "num": 11, "title": "Practical Methodology",
                    "sections": [
                        ("11.1", "Performance Metrics", []),
                        ("11.2", "Default Baseline Models", []),
                        ("11.3", "Determining Whether to Gather More Data", []),
                        ("11.4", "Selecting Hyperparameters", [
                            "11.4.1 Manual Hyperparameter Tuning",
                            "11.4.2 Automatic Hyperparameter Optimization Algorithms",
                            "11.4.3 Grid Search",
                            "11.4.4 Random Search",
                            "11.4.5 Model-Based Hyperparameter Optimization",
                        ]),
                        ("11.5", "Debugging Strategies", []),
                        ("11.6", "Example: Multi-Digit Number Recognition", []),
                    ],
                },
                {
                    "num": 12, "title": "Applications",
                    "sections": [
                        ("12.1", "Large Scale Deep Learning", [
                            "12.1.1 Fast CPU Implementations",
                            "12.1.2 GPU Implementations",
                            "12.1.3 Large Scale Distributed Implementations",
                            "12.1.4 Model Compression",
                            "12.1.5 Dynamic Structure",
                            "12.1.6 Specialized Hardware Implementations of Deep Networks",
                        ]),
                        ("12.2", "Computer Vision", [
                            "12.2.1 Preprocessing",
                            "12.2.2 Dataset Augmentation",
                        ]),
                        ("12.3", "Speech Recognition", []),
                        ("12.4", "Natural Language Processing", [
                            "12.4.1 n-grams",
                            "12.4.2 Neural Language Models",
                            "12.4.3 High-Dimensional Outputs",
                            "12.4.4 Combining Neural Language Models with n-grams",
                            "12.4.5 Neural Machine Translation",
                            "12.4.6 Historical Perspective",
                        ]),
                        ("12.5", "Other Applications", [
                            "12.5.1 Recommender Systems",
                            "12.5.2 Knowledge Representation, Reasoning and Question Answering",
                        ]),
                    ],
                },
            ],
        },
        {
            "name": "Part III — Deep Learning Research",
            "chapters": [
                {
                    "num": 13, "title": "Linear Factor Models",
                    "sections": [
                        ("13.1", "Probabilistic PCA and Factor Analysis", []),
                        ("13.2", "Independent Component Analysis (ICA)", []),
                        ("13.3", "Slow Feature Analysis", []),
                        ("13.4", "Sparse Coding", []),
                        ("13.5", "Manifold Interpretation of PCA", []),
                    ],
                },
                {
                    "num": 14, "title": "Autoencoders",
                    "sections": [
                        ("14.1", "Undercomplete Autoencoders", []),
                        ("14.2", "Regularized Autoencoders", [
                            "14.2.1 Sparse Autoencoders",
                            "14.2.2 Denoising Autoencoders",
                            "14.2.3 Regularizing by Penalizing Derivatives",
                        ]),
                        ("14.3", "Representational Power, Layer Size and Depth", []),
                        ("14.4", "Stochastic Encoders and Decoders", []),
                        ("14.5", "Denoising Autoencoders", ["14.5.1 Estimating the Score"]),
                        ("14.6", "Learning Manifolds with Autoencoders", []),
                        ("14.7", "Contractive Autoencoders", []),
                        ("14.8", "Predictive Sparse Decomposition", []),
                        ("14.9", "Applications of Autoencoders", []),
                    ],
                },
                {
                    "num": 15, "title": "Representation Learning",
                    "sections": [
                        ("15.1", "Greedy Layer-Wise Unsupervised Pretraining", [
                            "15.1.1 When and Why Does Unsupervised Pretraining Work?",
                        ]),
                        ("15.2", "Transfer Learning and Domain Adaptation", []),
                        ("15.3", "Semi-Supervised Disentangling of Causal Factors", []),
                        ("15.4", "Distributed Representation", []),
                        ("15.5", "Exponential Gains from Depth", []),
                        ("15.6", "Providing Clues to Discover Underlying Causes", []),
                    ],
                },
                {
                    "num": 16, "title": "Structured Probabilistic Models for Deep Learning",
                    "sections": [
                        ("16.1", "The Challenge of Unstructured Modeling", []),
                        ("16.2", "Using Graphs to Describe Model Structure", [
                            "16.2.1 Directed Models",
                            "16.2.2 Undirected Models",
                            "16.2.3 The Partition Function",
                            "16.2.4 Energy-Based Models",
                            "16.2.5 Separation and D-Separation",
                            "16.2.6 Converting between Undirected and Directed Graphs",
                            "16.2.7 Factor Graphs",
                        ]),
                        ("16.3", "Sampling from Graphical Models", []),
                        ("16.4", "Advantages of Structured Modeling", []),
                        ("16.5", "Learning about Dependencies", []),
                        ("16.6", "Inference and Approximate Inference", []),
                        ("16.7", "The Deep Learning Approach to Structured Probabilistic Models", [
                            "16.7.1 Example: The Restricted Boltzmann Machine",
                        ]),
                    ],
                },
                {
                    "num": 17, "title": "Monte Carlo Methods",
                    "sections": [
                        ("17.1", "Sampling and Monte Carlo Methods", [
                            "17.1.1 Why Sampling?",
                            "17.1.2 Basics of Monte Carlo Sampling",
                        ]),
                        ("17.2", "Importance Sampling", []),
                        ("17.3", "Markov Chain Monte Carlo Methods", []),
                        ("17.4", "Gibbs Sampling", []),
                        ("17.5", "The Challenge of Mixing between Separated Modes", [
                            "17.5.1 Tempering to Mix between Modes",
                            "17.5.2 Depth May Help Mixing",
                        ]),
                    ],
                },
                {
                    "num": 18, "title": "Confronting the Partition Function",
                    "sections": [
                        ("18.1", "The Log-Likelihood Gradient", []),
                        ("18.2", "Stochastic Maximum Likelihood and Contrastive Divergence", []),
                        ("18.3", "Pseudolikelihood", []),
                        ("18.4", "Score Matching and Ratio Matching", []),
                        ("18.5", "Denoising Score Matching", []),
                        ("18.6", "Noise-Contrastive Estimation", []),
                        ("18.7", "Estimating the Partition Function", [
                            "18.7.1 Annealed Importance Sampling",
                            "18.7.2 Bridge Sampling",
                        ]),
                    ],
                },
                {
                    "num": 19, "title": "Approximate Inference",
                    "sections": [
                        ("19.1", "Inference as Optimization", []),
                        ("19.2", "Expectation Maximization", []),
                        ("19.3", "MAP Inference and Sparse Coding", []),
                        ("19.4", "Variational Inference and Learning", [
                            "19.4.1 Discrete Latent Variables",
                            "19.4.2 Calculus of Variations",
                            "19.4.3 Continuous Latent Variables",
                            "19.4.4 Interactions between Learning and Inference",
                        ]),
                        ("19.5", "Learned Approximate Inference", [
                            "19.5.1 Wake-Sleep",
                            "19.5.2 Other Forms of Learned Inference",
                        ]),
                    ],
                },
                {
                    "num": 20, "title": "Deep Generative Models",
                    "sections": [
                        ("20.1", "Boltzmann Machines", []),
                        ("20.2", "Restricted Boltzmann Machines", [
                            "20.2.1 Conditional Distributions",
                            "20.2.2 Training Restricted Boltzmann Machines",
                        ]),
                        ("20.3", "Deep Belief Networks", []),
                        ("20.4", "Deep Boltzmann Machines", [
                            "20.4.1 Interesting Properties",
                            "20.4.2 DBM Mean Field Inference",
                            "20.4.3 DBM Parameter Learning",
                            "20.4.4 Layer-Wise Pretraining",
                            "20.4.5 Jointly Training Deep Boltzmann Machines",
                        ]),
                        ("20.5", "Boltzmann Machines for Real-Valued Data", [
                            "20.5.1 Gaussian-Bernoulli RBMs",
                            "20.5.2 Undirected Models of Conditional Covariance",
                        ]),
                        ("20.6", "Convolutional Boltzmann Machines", []),
                        ("20.7", "Boltzmann Machines for Structured or Sequential Outputs", []),
                        ("20.8", "Other Boltzmann Machines", []),
                        ("20.9", "Back-Propagation through Random Operations", [
                            "20.9.1 Back-Propagating through Discrete Stochastic Operations",
                        ]),
                        ("20.10", "Directed Generative Nets", [
                            "20.10.1 Sigmoid Belief Networks",
                            "20.10.2 Differentiable Generator Nets",
                            "20.10.3 Variational Autoencoders",
                            "20.10.4 Generative Adversarial Networks",
                            "20.10.5 Generative Moment Matching Networks",
                            "20.10.6 Convolutional Generative Networks",
                            "20.10.7 Auto-Regressive Networks",
                            "20.10.8 Linear Auto-Regressive Networks",
                            "20.10.9 Neural Auto-Regressive Networks",
                            "20.10.10 NADE",
                        ]),
                        ("20.11", "Drawing Samples from Autoencoders", [
                            "20.11.1 Markov Chain Associated with any Denoising Autoencoder",
                            "20.11.2 Clamping and the Conditional Distribution",
                            "20.11.3 Walk-Back Training Procedure",
                        ]),
                        ("20.12", "Generative Stochastic Networks", [
                            "20.12.1 Discriminative GSNs",
                        ]),
                        ("20.13", "Other Generation Schemes", []),
                        ("20.14", "Evaluating Generative Models", []),
                        ("20.15", "Conclusion", []),
                    ],
                },
            ],
        },
    ],
    "back": ["Bibliography", "Index"],
}


@app.route("/")
def index():
    return render_template("index.html", book=BOOK)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)), debug=True)
