{
  "asset_ids": [
    "1d48718453816204b8296b589a739b686b628ccbc33660a0fa008f622a1e6757",
    "861061a5d814040ba87ad2211ede8e3fd67fcc6af48a0c8eac4e06a74895b1e0"
  ],
  "digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
  "digests": [
    "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4"
  ],
  "project_name": "johnkday/nodegoat:latest",
  "results": [
    {
      "_sto_cortex_project_name": "johnkday/nodegoat:latest",
      "_sto_image_digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_id": "1d48718453816204b8296b589a739b686b628ccbc33660a0fa008f622a1e6757",
      "xdm.finding.asset_name": "johnkday/nodegoat:latest",
      "xdm.finding.asset_type": "Build Image",
      "xdm.finding.category": "VULNERABILITY",
      "xdm.finding.description": "Package apk-tools, version 2.10.6-r0, found on the Build Image sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4 (alpine 3.11.11), at file path: N/A is affected by CVE-2021-36159.",
      "xdm.finding.extended_fields": {
        "remediation": "Update the software apk-tools from version < 2.10.7-r0 to version 2.10.7-r0 as recommended by https://security.alpinelinux.org/vuln/CVE-2021-36159. Additional information can be found at https://nvd.nist.gov/vuln/detail/CVE-2021-36159."
      },
      "xdm.finding.id": "3b47adfee3ad96651b9a4ba2ac2b74ef",
      "xdm.finding.name": "Derived vulnerability found on asset",
      "xdm.finding.normalized_fields": {
        "xdm.disk.is_root": true,
        "xdm.disk.name": null,
        "xdm.disk.partition.id": null,
        "xdm.disk.partition.id_type": null,
        "xdm.file.path": "",
        "xdm.file.volume_path": null,
        "xdm.finding_sources": [
          "CORTEX_CLI_SCANNER"
        ],
        "xdm.host.found_in_vm_image": null,
        "xdm.host.hostname": null,
        "xdm.host.image": null,
        "xdm.host.ipv4_addresses": null,
        "xdm.host.ipv6_addresses": null,
        "xdm.host.mac_addresses": null,
        "xdm.host.os": null,
        "xdm.host.os_family": "linux",
        "xdm.software_package.file_creation": "1970-01-01T00:00:00Z",
        "xdm.software_package.id": "apk-tools",
        "xdm.software_package.installation_type": "USER",
        "xdm.software_package.is_in_use": false,
        "xdm.software_package.layer_id": "",
        "xdm.software_package.licenses": [
          "GPL2"
        ],
        "xdm.software_package.origin": "",
        "xdm.software_package.os_distribution": "alpine",
        "xdm.software_package.os_release": "3.11.11",
        "xdm.software_package.provider": "Natanael Copa <ncopa@alpinelinux.org>",
        "xdm.software_package.purl": "pkg:apk/alpine/apk-tools@2.10.6-r0",
        "xdm.software_package.symbols": null,
        "xdm.software_package.type": "PACKAGE",
        "xdm.software_package.version": "2.10.6-r0",
        "xdm.vulnerability.affected_versions": [
          "<2.10.7-r0"
        ],
        "xdm.vulnerability.cve_id": "CVE-2021-36159",
        "xdm.vulnerability.cve_risk_factors": [
          "Critical severity",
          "DoS - High",
          "Attack complexity: low",
          "Attack vector: network",
          "Exploit exists - POC",
          "Has fix"
        ],
        "xdm.vulnerability.cve_vendor_link": "https://security.alpinelinux.org/vuln/CVE-2021-36159",
        "xdm.vulnerability.cvss_score": 9.1,
        "xdm.vulnerability.cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H",
        "xdm.vulnerability.derived_from_base_image": false,
        "xdm.vulnerability.epss_score": 0.01,
        "xdm.vulnerability.exploitable": true,
        "xdm.vulnerability.fix_date": "1970-01-19T20:13:20.100000Z",
        "xdm.vulnerability.fix_versions": [
          "2.10.7-r0"
        ],
        "xdm.vulnerability.has_a_fix": true,
        "xdm.vulnerability.intelligence_id": "123f5b19-16cd-534d-a97a-8a38d766979a",
        "xdm.vulnerability.publish_date": "1970-01-19T20:13:20.108000Z",
        "xdm.vulnerability.severity": "CRITICAL",
        "xdm.vulnerability.status": "fixed"
      }
    },
    {
      "_sto_cortex_project_name": "johnkday/nodegoat:latest",
      "_sto_image_digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_id": "1d48718453816204b8296b589a739b686b628ccbc33660a0fa008f622a1e6757",
      "xdm.finding.asset_name": "johnkday/nodegoat:latest",
      "xdm.finding.asset_type": "Build Image",
      "xdm.finding.category": "VULNERABILITY",
      "xdm.finding.description": "Package openssl, version 1.1.1k-r0, found on the Build Image sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4 (alpine 3.11.11), at file path: N/A is affected by CVE-2023-3817.",
      "xdm.finding.extended_fields": {
        "remediation": "We were not able to determine a specific fix for this vulnerability. To check for the most up-to-date guidance on workarounds or fixes please consult https://security.alpinelinux.org/vuln/CVE-2023-3817. Additional information can be found at https://nvd.nist.gov/vuln/detail/CVE-2023-3817."
      },
      "xdm.finding.id": "3be3cae7beb593c41366eb2e5ecf52ff",
      "xdm.finding.name": "Derived vulnerability found on asset",
      "xdm.finding.normalized_fields": {
        "xdm.disk.is_root": true,
        "xdm.disk.name": null,
        "xdm.disk.partition.id": null,
        "xdm.disk.partition.id_type": null,
        "xdm.file.path": "",
        "xdm.file.volume_path": null,
        "xdm.finding_sources": [
          "CORTEX_CLI_SCANNER"
        ],
        "xdm.host.found_in_vm_image": null,
        "xdm.host.hostname": null,
        "xdm.host.image": null,
        "xdm.host.ipv4_addresses": null,
        "xdm.host.ipv6_addresses": null,
        "xdm.host.mac_addresses": null,
        "xdm.host.os": null,
        "xdm.host.os_family": "linux",
        "xdm.software_package.file_creation": "1970-01-01T00:00:00Z",
        "xdm.software_package.id": "openssl",
        "xdm.software_package.installation_type": "USER",
        "xdm.software_package.is_in_use": false,
        "xdm.software_package.layer_id": "",
        "xdm.software_package.licenses": [
          "OpenSSL"
        ],
        "xdm.software_package.origin": "",
        "xdm.software_package.os_distribution": "alpine",
        "xdm.software_package.os_release": "3.11.11",
        "xdm.software_package.provider": "Timo Teras <timo.teras@iki.fi>",
        "xdm.software_package.purl": "pkg:apk/alpine/openssl@1.1.1k-r0",
        "xdm.software_package.symbols": null,
        "xdm.software_package.type": "PACKAGE",
        "xdm.software_package.version": "1.1.1k-r0",
        "xdm.vulnerability.affected_versions": [
          "<=1.1.1u",
          ">=1.1.1"
        ],
        "xdm.vulnerability.cve_id": "CVE-2023-3817",
        "xdm.vulnerability.cve_risk_factors": [
          "Attack vector: network",
          "Medium severity",
          "DoS - Low",
          "Attack complexity: low"
        ],
        "xdm.vulnerability.cve_vendor_link": "https://security.alpinelinux.org/vuln/CVE-2023-3817",
        "xdm.vulnerability.cvss_score": 5.3,
        "xdm.vulnerability.cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L",
        "xdm.vulnerability.derived_from_base_image": false,
        "xdm.vulnerability.epss_score": 0,
        "xdm.vulnerability.exploitable": false,
        "xdm.vulnerability.fix_date": null,
        "xdm.vulnerability.fix_versions": null,
        "xdm.vulnerability.has_a_fix": false,
        "xdm.vulnerability.intelligence_id": "e17f83da-e745-56a8-8e2b-4966ba0336db",
        "xdm.vulnerability.publish_date": "1970-01-20T13:39:21.600000Z",
        "xdm.vulnerability.severity": "MEDIUM",
        "xdm.vulnerability.status": null
      }
    },
    {
      "_sto_cortex_project_name": "johnkday/nodegoat:latest",
      "_sto_image_digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_id": "1d48718453816204b8296b589a739b686b628ccbc33660a0fa008f622a1e6757",
      "xdm.finding.asset_name": "johnkday/nodegoat:latest",
      "xdm.finding.asset_type": "Build Image",
      "xdm.finding.category": "VULNERABILITY",
      "xdm.finding.description": "Package busybox, version 1.31.1-r10, found on the Build Image sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4 (alpine 3.11.11), at file path: N/A is affected by CVE-2025-60876.",
      "xdm.finding.extended_fields": {
        "remediation": "We were not able to determine a specific fix for this vulnerability. To check for the most up-to-date guidance on workarounds or fixes please consult https://security.alpinelinux.org/vuln/CVE-2025-60876. Additional information can be found at https://nvd.nist.gov/vuln/detail/CVE-2025-60876."
      },
      "xdm.finding.id": "54032f02a7a6d8904c7504a58398f0f7",
      "xdm.finding.name": "Derived vulnerability found on asset",
      "xdm.finding.normalized_fields": {
        "xdm.disk.is_root": true,
        "xdm.disk.name": null,
        "xdm.disk.partition.id": null,
        "xdm.disk.partition.id_type": null,
        "xdm.file.path": "",
        "xdm.file.volume_path": null,
        "xdm.finding_sources": [
          "CORTEX_CLI_SCANNER"
        ],
        "xdm.host.found_in_vm_image": null,
        "xdm.host.hostname": null,
        "xdm.host.image": null,
        "xdm.host.ipv4_addresses": null,
        "xdm.host.ipv6_addresses": null,
        "xdm.host.mac_addresses": null,
        "xdm.host.os": null,
        "xdm.host.os_family": "linux",
        "xdm.software_package.file_creation": "1970-01-01T00:00:00Z",
        "xdm.software_package.id": "busybox",
        "xdm.software_package.installation_type": "USER",
        "xdm.software_package.is_in_use": false,
        "xdm.software_package.layer_id": "",
        "xdm.software_package.licenses": [
          "GPL-2.0-only"
        ],
        "xdm.software_package.origin": "",
        "xdm.software_package.os_distribution": "alpine",
        "xdm.software_package.os_release": "3.11.11",
        "xdm.software_package.provider": "Natanael Copa <ncopa@alpinelinux.org>",
        "xdm.software_package.purl": "pkg:apk/alpine/busybox@1.31.1-r10",
        "xdm.software_package.symbols": null,
        "xdm.software_package.type": "PACKAGE",
        "xdm.software_package.version": "1.31.1-r10",
        "xdm.vulnerability.affected_versions": [
          "<=1.37.0"
        ],
        "xdm.vulnerability.cve_id": "CVE-2025-60876",
        "xdm.vulnerability.cve_risk_factors": [
          "Exploit exists - POC",
          "Recent vulnerability",
          "Attack complexity: low",
          "Attack vector: network"
        ],
        "xdm.vulnerability.cve_vendor_link": "https://security.alpinelinux.org/vuln/CVE-2025-60876",
        "xdm.vulnerability.cvss_score": 0,
        "xdm.vulnerability.cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N",
        "xdm.vulnerability.derived_from_base_image": false,
        "xdm.vulnerability.epss_score": 0,
        "xdm.vulnerability.exploitable": true,
        "xdm.vulnerability.fix_date": null,
        "xdm.vulnerability.fix_versions": null,
        "xdm.vulnerability.has_a_fix": false,
        "xdm.vulnerability.intelligence_id": "213743d1-e178-590b-b9a7-b183d0c42d0b",
        "xdm.vulnerability.publish_date": "1970-01-21T09:38:52.800000Z",
        "xdm.vulnerability.severity": "LOW",
        "xdm.vulnerability.status": null
      }
    },
    {
      "_sto_cortex_project_name": "johnkday/nodegoat:latest",
      "_sto_image_digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_id": "861061a5d814040ba87ad2211ede8e3fd67fcc6af48a0c8eac4e06a74895b1e0",
      "xdm.finding.asset_name": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_type": "Core Image",
      "xdm.finding.category": "VULNERABILITY",
      "xdm.finding.description": "Package apk-tools, version 2.10.6-r0, found on the Core Image sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4 (alpine 3.11.11), at file path: N/A is affected by CVE-2021-36159.",
      "xdm.finding.extended_fields": {
        "remediation": "Update the software apk-tools from version < 2.10.7-r0 to version 2.10.7-r0 as recommended by https://security.alpinelinux.org/vuln/CVE-2021-36159. Additional information can be found at https://nvd.nist.gov/vuln/detail/CVE-2021-36159."
      },
      "xdm.finding.id": "f78984684a2aab6472f413b503e6383d",
      "xdm.finding.name": "Vulnerability found on an Asset",
      "xdm.finding.normalized_fields": {
        "xdm.disk.is_root": true,
        "xdm.disk.name": null,
        "xdm.disk.partition.id": null,
        "xdm.disk.partition.id_type": null,
        "xdm.file.path": "",
        "xdm.file.volume_path": null,
        "xdm.finding_sources": [
          "CORTEX_CLI_SCANNER"
        ],
        "xdm.host.found_in_vm_image": null,
        "xdm.host.hostname": null,
        "xdm.host.image": null,
        "xdm.host.ipv4_addresses": null,
        "xdm.host.ipv6_addresses": null,
        "xdm.host.mac_addresses": null,
        "xdm.host.os": null,
        "xdm.host.os_family": "linux",
        "xdm.software_package.file_creation": "1970-01-01T00:00:00Z",
        "xdm.software_package.id": "apk-tools",
        "xdm.software_package.installation_type": "USER",
        "xdm.software_package.is_in_use": false,
        "xdm.software_package.layer_id": "",
        "xdm.software_package.licenses": [
          "GPL2"
        ],
        "xdm.software_package.origin": "",
        "xdm.software_package.os_distribution": "alpine",
        "xdm.software_package.os_release": "3.11.11",
        "xdm.software_package.provider": "Natanael Copa <ncopa@alpinelinux.org>",
        "xdm.software_package.purl": "pkg:apk/alpine/apk-tools@2.10.6-r0",
        "xdm.software_package.symbols": null,
        "xdm.software_package.type": "PACKAGE",
        "xdm.software_package.version": "2.10.6-r0",
        "xdm.vulnerability.affected_versions": [
          "<2.10.7-r0"
        ],
        "xdm.vulnerability.cve_id": "CVE-2021-36159",
        "xdm.vulnerability.cve_risk_factors": [
          "Critical severity",
          "DoS - High",
          "Attack complexity: low",
          "Attack vector: network",
          "Exploit exists - POC",
          "Has fix"
        ],
        "xdm.vulnerability.cve_vendor_link": "https://security.alpinelinux.org/vuln/CVE-2021-36159",
        "xdm.vulnerability.cvss_score": 9.1,
        "xdm.vulnerability.cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H",
        "xdm.vulnerability.derived_from_base_image": false,
        "xdm.vulnerability.epss_score": 0.01,
        "xdm.vulnerability.exploitable": true,
        "xdm.vulnerability.fix_date": "1970-01-19T20:13:20.100000Z",
        "xdm.vulnerability.fix_versions": [
          "2.10.7-r0"
        ],
        "xdm.vulnerability.has_a_fix": true,
        "xdm.vulnerability.intelligence_id": "123f5b19-16cd-534d-a97a-8a38d766979a",
        "xdm.vulnerability.publish_date": "1970-01-19T20:13:20.108000Z",
        "xdm.vulnerability.severity": "CRITICAL",
        "xdm.vulnerability.status": "fixed"
      }
    },
    {
      "_sto_cortex_project_name": "johnkday/nodegoat:latest",
      "_sto_image_digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_id": "1d48718453816204b8296b589a739b686b628ccbc33660a0fa008f622a1e6757",
      "xdm.finding.asset_name": "johnkday/nodegoat:latest",
      "xdm.finding.asset_type": "Build Image",
      "xdm.finding.category": "VULNERABILITY",
      "xdm.finding.description": "Package openssl, version 1.1.1k-r0, found on the Build Image sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4 (alpine 3.11.11), at file path: N/A is affected by CVE-2023-3817.",
      "xdm.finding.extended_fields": {
        "remediation": "We were not able to determine a specific fix for this vulnerability. To check for the most up-to-date guidance on workarounds or fixes please consult https://security.alpinelinux.org/vuln/CVE-2023-3817. Additional information can be found at https://nvd.nist.gov/vuln/detail/CVE-2023-3817."
      },
      "xdm.finding.id": "3be3cae7beb593c41366eb2e5ecf52ff-namefb",
      "xdm.finding.name": "Derived vulnerability found on asset",
      "xdm.finding.normalized_fields": {
        "xdm.disk.is_root": true,
        "xdm.disk.name": null,
        "xdm.disk.partition.id": null,
        "xdm.disk.partition.id_type": null,
        "xdm.file.path": "",
        "xdm.file.volume_path": null,
        "xdm.finding_sources": [
          "CORTEX_CLI_SCANNER"
        ],
        "xdm.host.found_in_vm_image": null,
        "xdm.host.hostname": null,
        "xdm.host.image": null,
        "xdm.host.ipv4_addresses": null,
        "xdm.host.ipv6_addresses": null,
        "xdm.host.mac_addresses": null,
        "xdm.host.os": null,
        "xdm.host.os_family": "linux",
        "xdm.software_package.file_creation": "1970-01-01T00:00:00Z",
        "xdm.software_package.installation_type": "USER",
        "xdm.software_package.is_in_use": false,
        "xdm.software_package.layer_id": "",
        "xdm.software_package.licenses": [
          "OpenSSL"
        ],
        "xdm.software_package.name": "openssl",
        "xdm.software_package.origin": "",
        "xdm.software_package.os_distribution": "alpine",
        "xdm.software_package.os_release": "3.11.11",
        "xdm.software_package.provider": "Timo Teras <timo.teras@iki.fi>",
        "xdm.software_package.purl": "pkg:apk/alpine/openssl@1.1.1k-r0",
        "xdm.software_package.symbols": null,
        "xdm.software_package.type": "PACKAGE",
        "xdm.software_package.version": "1.1.1k-r0",
        "xdm.vulnerability.affected_versions": [
          "<=1.1.1u",
          ">=1.1.1"
        ],
        "xdm.vulnerability.cve_id": "CVE-2099-NAMEFB",
        "xdm.vulnerability.cve_risk_factors": [
          "Attack vector: network",
          "Medium severity",
          "DoS - Low",
          "Attack complexity: low"
        ],
        "xdm.vulnerability.cve_vendor_link": "https://security.alpinelinux.org/vuln/CVE-2023-3817",
        "xdm.vulnerability.cvss_score": 5.3,
        "xdm.vulnerability.cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L",
        "xdm.vulnerability.derived_from_base_image": false,
        "xdm.vulnerability.epss_score": 0,
        "xdm.vulnerability.exploitable": false,
        "xdm.vulnerability.fix_date": null,
        "xdm.vulnerability.fix_versions": null,
        "xdm.vulnerability.has_a_fix": false,
        "xdm.vulnerability.intelligence_id": "e17f83da-e745-56a8-8e2b-4966ba0336db",
        "xdm.vulnerability.publish_date": "1970-01-20T13:39:21.600000Z",
        "xdm.vulnerability.severity": "MEDIUM",
        "xdm.vulnerability.status": null
      }
    },
    {
      "_sto_cortex_project_name": "johnkday/nodegoat:latest",
      "_sto_image_digest": "sha256:69dc078a1fa155ff4c77ee6a0e51414a5c36f9745cefff0b5db659727add04f4",
      "xdm.finding.asset_id": "1d48718453816204b8296b589a739b686b628ccbc33660a0fa008f622a1e6757",
      "xdm.finding.asset_name": "johnkday/nodegoat:latest",
      "xdm.finding.asset_type": "Build Image",
      "xdm.finding.category": "DATA",
      "xdm.finding.description": "AWS access key found in image layer.",
      "xdm.finding.id": "finding-secret-001",
      "xdm.finding.normalized_fields": {
        "xdm.file.path": "/app/config/credentials.txt",
        "xdm.file.position.start.character": 4,
        "xdm.file.position.start.line": 12,
        "xdm.secret.layer_id": "sha256:layerLayerLayer",
        "xdm.secret.secret_type": "AWS Access Key",
        "xdm.secret.snippet": "AKIAIOSFODNN7EXAMPLE",
        "xdm.secret.unique_identifier": "AKIA123456789012"
      }
    },
    {
      "xdm.finding.category": "COMPLIANCE",
      "xdm.finding.id": "finding-skip-001",
      "xdm.finding.normalized_fields": {}
    }
  ]
}