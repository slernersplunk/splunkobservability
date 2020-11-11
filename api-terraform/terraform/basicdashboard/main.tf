# Creates a dashboard group called Terraform Dashboard Group and a dashboard called Terraform Dashboard with a CPU chart
# Configure the SignalFx provider
provider "signalfx" {
  auth_token = "YOURTOKENHERE"
  # If your organization uses a different realm
  api_url = "https://api.YOURREALMHERE.signalfx.com"
}

resource "signalfx_dashboard_group" "tfgroup" {
    name = "Terraform Dashboard Group"
    description = "Terraform Dashboard Group"
}

resource "signalfx_time_chart" "CPUUtil" {
    name = "CPU Utilization"

    program_text = <<-EOF
        data("cpu.utilization").publish(label="CPU Utilization")
        EOF
}

resource "signalfx_dashboard" "tfdashboard" {
    name = "Terraform Dashboard"
    dashboard_group = signalfx_dashboard_group.tfgroup.id

    chart {
        chart_id = signalfx_time_chart.CPUUtil.id
    }
}
