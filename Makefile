# 'make' by itself runs the 'run' target
.DEFAULT_GOAL := run

.PHONY: run
run: lint get_rd_rt l3vpn_prompt unit iac

.PHONY: lint
lint:
	@echo "############## Starting  lint ##############"
	find . -name "*_playbook.yml" | xargs ansible-lint
	@echo "Completed lint"

.PHONY: get_rd_rt
get_rd_rt:
	@echo "############## Starting playbook to get rd rt values ##############"
	ansible-playbook get_rd_rt_playbook.yml
	@echo "Completed playbook to get rd rt values"

.PHONY: l3vpn_prompt
l3vpn_prompt:
	@echo "############## Starting playbook to get l3vpn details via prompt ##############"
	ansible-playbook get_l3vpn_prompt_playbook.yml
	@echo "Completed playbook to get l3vpn details via prompt"

.PHONY: unit
unit:
	@echo "############## Starting  unit tests ##############"
	ansible-playbook iosxr_l3vpn_unittest.yml
	@echo "Completed unit tests"


.PHONY: iac
iac:
	@echo "############## Starting l3vpn infra as a code ##############"
	ansible-playbook iosxr_l3vpn_iac_playbook.yml
	@echo "Completed l3vpn infra as a code"
