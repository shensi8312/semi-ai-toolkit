<p align="center">
  <h1 align="center">Semi-AI-Toolkit</h1>
  <p align="center">
    <strong>Open-source AI tools for semiconductor equipment — from design to mass production.</strong>
  </p>
  <p align="center">
    <a href="https://ai-mst.com">Website</a> &middot;
    <a href="#features">Features</a> &middot;
    <a href="#quick-start">Quick Start</a> &middot;
    <a href="#contributing">Contributing</a> &middot;
    <a href="#license">License</a>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
    <img src="https://img.shields.io/badge/license-Apache%202.0-green" alt="License: Apache 2.0">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome">
  </p>
</p>

---

## Overview

**Semi-AI-Toolkit** is an open-source collection of AI-powered tools and example pipelines designed specifically for the semiconductor equipment industry. Whether you are working on process optimization, equipment monitoring, or intelligent manufacturing, this toolkit provides practical, production-oriented building blocks to accelerate your AI adoption.

<!-- 半导体设备 AI 工具集：覆盖 P&ID 解析、DOE 优化、虚拟量测、数据预处理等核心场景 -->

Built and maintained by [MST Semiconductor (集芯科技)](https://ai-mst.com), this project reflects our mission of empowering semiconductor equipment with AI — from design through high-volume manufacturing.

---

## Features

| Module | Description | Key Tech |
|--------|-------------|----------|
| **P&ID Parser** | Intelligent parsing and symbol recognition for Piping & Instrumentation Diagrams | OpenCV, YOLOv8 |
| **DOE Optimizer** | Bayesian optimization for Design of Experiments in process tuning | SciPy, BoTorch |
| **Virtual Metrology (VM) Pipeline** | End-to-end model training pipeline for virtual metrology | PyTorch, scikit-learn |
| **Equipment Data Preprocessor** | Sensor signal cleaning, alignment, and feature extraction utilities | pandas, NumPy |

### P&ID Parser
<!-- P&ID 图智能解析：自动识别阀门、传感器、管路等元素 -->
Automatically detect and classify symbols (valves, sensors, pipelines, etc.) from engineering P&ID drawings. Outputs structured JSON for downstream integration with design tools.

### DOE Optimizer
<!-- DOE 实验设计优化器：基于贝叶斯优化，减少实验次数，加速工艺调优 -->
Reduce the number of physical experiments needed to find optimal process parameters. Leverages Bayesian optimization with Gaussian Process surrogates to intelligently explore the parameter space.

### Virtual Metrology Pipeline
<!-- 虚拟量测模型训练流水线：用设备传感器数据预测产品质量 -->
Train predictive models that estimate wafer quality metrics from equipment sensor data — eliminating the need for costly inline measurements on every wafer.

### Equipment Data Preprocessor
<!-- 设备数据预处理工具：信号清洗、对齐、特征提取 -->
A collection of utilities for handling real-world semiconductor equipment data: timestamp alignment, outlier removal, signal segmentation, and automated feature extraction.

---

## Quick Start

### Installation

```bash
pip install semi-ai-toolkit
```

Or install from source:

```bash
git clone https://github.com/ai-mst/semi-ai-toolkit.git
cd semi-ai-toolkit
pip install -e ".[dev]"
```

### Requirements

- Python >= 3.9
- See `requirements.txt` for full dependency list

### Usage Examples

#### 1. P&ID Symbol Detection

```python
from semi_ai_toolkit.pid import PIDParser

parser = PIDParser(model="yolov8-pid-symbols")
results = parser.parse("drawings/reactor_pid.png")

for symbol in results.symbols:
    print(f"[{symbol.label}] confidence={symbol.score:.2f}  bbox={symbol.bbox}")

# Export structured output
# 导出结构化 JSON，可对接下游设计工具
results.to_json("output/reactor_symbols.json")
```

#### 2. Bayesian DOE Optimization

```python
from semi_ai_toolkit.doe import BayesianDOE

# Define parameter space（定义工艺参数空间）
param_space = {
    "temperature": (200.0, 400.0),     # degC
    "pressure":    (1.0, 10.0),        # Torr
    "rf_power":    (100.0, 500.0),     # W
}

optimizer = BayesianDOE(param_space, objective="minimize")

# Run optimization loop（运行优化循环）
for trial in range(20):
    next_params = optimizer.suggest()
    # Run actual experiment or simulation...
    result = run_experiment(next_params)  # your function
    optimizer.observe(next_params, result)

print("Best parameters found:", optimizer.best_params)
print("Best objective value: ", optimizer.best_value)
```

#### 3. Virtual Metrology Model Training

```python
from semi_ai_toolkit.vm import VMPipeline

# Load equipment sensor data and metrology targets
# 加载设备传感器数据和量测目标值
pipeline = VMPipeline.from_csv(
    sensors="data/equipment_sensors.csv",
    targets="data/metrology_targets.csv",
)

# Train and evaluate（训练并评估模型）
pipeline.preprocess(normalize=True, remove_outliers=True)
model = pipeline.train(
    model_type="lstm",       # or "xgboost", "transformer"
    epochs=50,
    batch_size=64,
)

metrics = pipeline.evaluate(model)
print(f"VM Model - MAE: {metrics['mae']:.4f}, R2: {metrics['r2']:.4f}")

# Save for deployment（保存模型用于部署）
pipeline.export(model, "models/vm_etch_rate.pt")
```

#### 4. Equipment Data Preprocessing

```python
from semi_ai_toolkit.preprocess import EquipmentDataProcessor

processor = EquipmentDataProcessor()

# Load raw sensor logs（加载原始传感器日志）
df = processor.load("data/raw_sensor_log.csv")

# Clean and align（清洗、对齐、特征提取）
df = processor.remove_outliers(df, method="iqr", threshold=3.0)
df = processor.align_timestamps(df, freq="100ms")
features = processor.extract_features(df, window="5s", stats=["mean", "std", "slope"])

print(f"Extracted {features.shape[1]} features from {features.shape[0]} samples")
features.to_parquet("data/processed_features.parquet")
```

---

## Tech Stack

| Category | Libraries |
|----------|-----------|
| Deep Learning | PyTorch, ONNX Runtime |
| Machine Learning | scikit-learn, XGBoost, BoTorch |
| Computer Vision | OpenCV, Ultralytics (YOLOv8) |
| Scientific Computing | NumPy, SciPy, pandas |
| Visualization | Matplotlib, Plotly |
| Data Formats | Parquet, HDF5, SECS/GEM |

---

## Project Structure

```
semi-ai-toolkit/
├── semi_ai_toolkit/
│   ├── pid/              # P&ID parsing module
│   ├── doe/              # DOE optimization module
│   ├── vm/               # Virtual metrology pipeline
│   ├── preprocess/       # Data preprocessing utilities
│   └── utils/            # Shared helpers
├── examples/             # Jupyter notebook examples
├── tests/                # Unit and integration tests
├── docs/                 # Documentation
├── requirements.txt
├── setup.py
└── README.md
```

---

## Contributing

We welcome contributions from the semiconductor and AI communities! Here is how you can get involved:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes with clear messages: `git commit -m "feat: add new DOE acquisition function"`
4. **Push** to your fork: `git push origin feature/your-feature-name`
5. **Open a Pull Request** against `main`

### Development Setup

```bash
git clone https://github.com/ai-mst/semi-ai-toolkit.git
cd semi-ai-toolkit
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/
```

### Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style conventions
- Add unit tests for new features
- Update documentation when modifying public APIs
- Keep PRs focused — one feature or fix per PR

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

---

## About MST Semiconductor (集芯科技)

**MST Semiconductor** (迈烁集芯（上海）科技有限公司) is an AI-native semiconductor equipment technology company. We build intelligent software solutions that span the entire semiconductor equipment lifecycle — from concept design and simulation through process development and high-volume manufacturing.

Our core belief: **AI should be deeply embedded in semiconductor equipment, not bolted on as an afterthought.**

We work at the intersection of domain expertise in semiconductor processes and state-of-the-art AI/ML, delivering tangible improvements in yield, throughput, and equipment uptime for fabs and equipment makers worldwide.

Learn more at **[https://ai-mst.com](https://ai-mst.com)**

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).

```
Copyright 2025-2026 MST Semiconductor (迈烁集芯（上海）科技有限公司)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---

## Contact

- **Email:** [contact@ai-mst.com](mailto:contact@ai-mst.com)
- **Website:** [https://ai-mst.com](https://ai-mst.com)
- **GitHub Issues:** For bug reports and feature requests, please use [GitHub Issues](https://github.com/ai-mst/semi-ai-toolkit/issues)

---

<p align="center">
  Built with precision by <a href="https://ai-mst.com">MST Semiconductor (集芯科技)</a>
</p>
