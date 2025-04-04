## **1. Checklist for Identifying Risk in US Bank Transactions**

### **A. Entity-Level Checks**  
#### **1. Individuals (People)**
- ☐ Check against **OFAC Sanctions List (SDN, non-SDN lists)**  
- ☐ Verify identity using **SSN, date of birth, and public records**  
- ☐ Look for **politically exposed persons (PEPs)**  
- ☐ Identify **negative news/media mentions** (criminal records, fraud, financial crimes)  
- ☐ Verify against **Interpol, FBI most-wanted lists**  
- ☐ Check involvement in **past financial fraud, money laundering, Ponzi schemes**  
- ☐ Cross-check with **terrorism financing databases (FinCEN, FATF, World Bank, etc.)**  
- ☐ Check for **sudden unexplained wealth, shell entities, or offshore tax havens**  
- ☐ Identify **multiple accounts linked to one person (potential identity fraud)**  

#### **2. Companies / Business Entities**  
- ☐ Check against **OFAC Sanctions List & BIS Entity List**  
- ☐ Verify corporate identity via **SEC filings, FINCEN Beneficial Ownership Registry**  
- ☐ Identify **shell companies, subsidiaries in high-risk jurisdictions**  
- ☐ Check for **high cash transactions, no valid business operations (red flag for laundering)**  
- ☐ Identify **directors/owners linked to past fraud, tax evasion, or legal cases**  
- ☐ Verify presence in **Panama Papers, Pandora Papers, or other leaked datasets**  
- ☐ Check against **adverse media for financial crime, corruption, or human trafficking**  
- ☐ Identify **frequent wire transfers to high-risk or sanctioned regions**  
- ☐ Look for **abnormal financial patterns (frequent round-tripping, layering)**  

---

### **B. Transaction-Level Checks**  
- ☐ **High-risk transaction types:** Cryptocurrency, casinos, money remitters, shell firms.  
- ☐ **Large, sudden transactions** without clear business justification.  
- ☐ **Frequent transactions just below reporting threshold (structuring/smurfing).**  
- ☐ **Wire transfers to/from high-risk countries (as per FATF).**  
- ☐ **Multiple transactions with sanctioned or embargoed regions.**  
- ☐ **Frequent ATM withdrawals from multiple locations (potential fraud/structuring).**  
- ☐ **Transaction memo descriptions hinting at suspicious activity (e.g., “consulting,” “gift,” “loan repayment” without documentation).**  
- ☐ **Use of anonymous payment methods (crypto, prepaid cards).**  
- ☐ **Suspicious correspondent banking transactions (involving multiple intermediary banks).**  
- ☐ **Round-trip transactions (money moving between same parties in different locations).**  
- ☐ **Transactions linked to known criminal enterprises, darknet markets, or scams.**  
- ☐ **Multiple beneficiaries receiving funds from a single entity (possible layering tactic).**  
- ☐ **Rapid inflows and outflows without clear economic rationale.**  
- ☐ **Usage of secret channels like VPN.**  

---

## **2. Risk Rating Strategy (0-1 Scale)**  
**Higher risk transactions score closer to 1; lower risk transactions score closer to 0.**  

| **Risk Factor**                        | **Weight (%)** | **Score (0-1 scale)** |
|--------------------------------------|------------|------------------|
| **Entity Sanctions (OFAC, BIS, FATF, etc.)** | 25% | 0 (clean) to 1 (sanctioned) |
| **Adverse Media Mentions (Fraud, Crime, etc.)** | 20% | 0 (clean) to 1 (criminal history) |
| **PEP (Politically Exposed Person) Risk** | 15% | 0 (not PEP) to 1 (high-ranking PEP) |
| **High-Risk Jurisdiction Transactions** | 15% | 0 (low-risk country) to 1 (high-risk country) |
| **Suspicious Transaction Patterns** | 15% | 0 (normal) to 1 (layering/round-tripping) |
| **Anonymity / Shell Company Link** | 10% | 0 (legitimate company) to 1 (shell entity) |

**Final Risk Score Calculation:**  
- **Score = (Sanction Score × 0.25) + (Adverse Media × 0.20) + (PEP Score × 0.15) + (Jurisdiction Score × 0.15) + (Transaction Pattern Score × 0.15) + (Shell Company Score × 0.10)**  

**Thresholds:**  
- **0 - 0.3 → Low Risk**  
- **0.31 - 0.6 → Medium Risk**  
- **0.61 - 1.0 → High Risk (Requires Review/Investigation)**  

---

## **3. Confidence Rating Strategy (0-1 Scale)**  
**Measures the reliability of the risk score based on data completeness & verification strength.**  

| **Confidence Factor**                  | **Weight (%)** | **Score (0-1 scale)** |
|----------------------------------------|------------|------------------|
| **Data Source Credibility (Official vs. Unverified)** | 25% | 0 (low credibility) to 1 (official records) |
| **Entity Identity Verification (KYC, Beneficial Ownership)** | 20% | 0 (unverified) to 1 (fully verified) |
| **Transaction Pattern Consistency** | 15% | 0 (unknown) to 1 (clear pattern detected) |
| **Cross-Reference with Multiple Sources** | 15% | 0 (single source) to 1 (multiple confirmations) |
| **Timeliness of Data (Recent vs. Old Records)** | 15% | 0 (outdated) to 1 (real-time data) |
| **Historical Accuracy of Risk Predictions** | 10% | 0 (inconsistent) to 1 (highly accurate model)** |

**Final Confidence Score Calculation:**  
- **Score = (Source Credibility × 0.25) + (Identity Verification × 0.20) + (Pattern Consistency × 0.15) + (Cross-Reference × 0.15) + (Timeliness × 0.15) + (Historical Accuracy × 0.10)**  

**Thresholds:**  
- **0 - 0.3 → Low Confidence (Risk score may not be reliable)**  
- **0.31 - 0.6 → Medium Confidence (Needs additional verification)**  
- **0.61 - 1.0 → High Confidence (Strong data reliability)**  

---

### **How to Use This?**  
- **Entities with risk scores > 0.6 should be flagged for enhanced due diligence.**  
- **Transactions with high-risk elements should trigger Suspicious Activity Reports (SARs).**  
- **Confidence rating helps analysts prioritize verification efforts.**  
  - **High-confidence, high-risk → Immediate action required.**  
  - **Low-confidence, high-risk → More data needed before action.**  

---
